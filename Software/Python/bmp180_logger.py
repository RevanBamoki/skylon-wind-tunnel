#!/usr/bin/env python3
"""
Dual-BMP180 live dashboard + CSV logger
  • Uno  → COM5   (T1 , P1)
  • Nano → COM4   (T2 , P2)
"""

import csv, time, math, serial
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ── USER SETTINGS ────────────────────────────────────────────────────────────
UNO_PORT   = 'COM5'
NANO_PORT  = 'COM4'
BAUD_RATE  = 9_600

CSV_FILE   = 'bmp_dual_log.csv'
LOG_TO_CSV = True

SAMPLE_HZ        = 20                  # Hz   ⇒ 100 ms interval
SMOOTH_WINDOW    = 1                   # samples
HISTORY_SAMPLES  = 300                 # points on screen
XTICK_SPACING_S  = 5                   # seconds (x–axis tick every 5 s)
RE_Y_EXPAND      = 1.05                # expand Re axis 5 % top & bottom
# ─────────────────────────────────────────────────────────────────────────────

# physical constants / geometry
R_AIR = 287.05         # J kg-1 K-1
MU_AIR = 1.81e-5       # Pa s
CHORD  = 0.058          # m

# ── serial ­──────────────────────────────────────────────────────────────────
ser1 = serial.Serial(UNO_PORT , BAUD_RATE, timeout=1)
ser2 = serial.Serial(NANO_PORT, BAUD_RATE, timeout=1)

# rolling buffers
def dq(): return deque(maxlen=HISTORY_SAMPLES)
t_buf = dq()
T1_buf = dq(); P1_buf = dq()
T2_buf = dq(); P2_buf = dq()
dP_buf = dq(); U_buf  = dq()
E_buf  = dq(); Re_buf = dq()

T1_raw = deque(maxlen=SMOOTH_WINDOW)
T2_raw = deque(maxlen=SMOOTH_WINDOW)
P1_raw = deque(maxlen=SMOOTH_WINDOW)
P2_raw = deque(maxlen=SMOOTH_WINDOW)

def smooth(buf, v):
    buf.append(v)
    return sum(buf)/len(buf)

# CSV log
if LOG_TO_CSV:
    csv_f = open(CSV_FILE, 'w', newline='')
    writer = csv.writer(csv_f)
    writer.writerow(
        ['t_s','T1_C','P1_Pa','T2_C','P2_Pa','dP_Pa','U_m_s','E_loss_Jkg','Re']
    )

# ── Matplotlib figure ­───────────────────────────────────────────────────────
fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=True)
axT, axP, axD, axR = axes

# ── coloured line objects (requirements 1-4) ────────────────────────────────
l_T1, = axT.plot([], [], color='blue' , label='T1 Uno')
l_T2, = axT.plot([], [], color='orange', label='T2 Nano')
axT.set_ylabel('°C'); axT.set_title('Temperature (°C)')

l_P1, = axP.plot([], [], color='red'  , label='P1 Uno')
l_P2, = axP.plot([], [], color='green', label='P2 Nano')
axP.set_ylabel('Pa'); axP.set_title('Pressure (Pa)')

l_dP, = axD.plot([], [], color='yellow', label='ΔP (Pa)')
l_U ,  = axD.plot([], [], color='purple', label='U (m s⁻¹)')
l_E ,  = axD.plot([], [], color='grey'  , label='E_loss (J kg⁻¹)')
axD.set_ylabel('mixed units'); axD.set_title('ΔP • U • E_loss')

l_Re , = axR.plot([], [], color='black', label='Re')
axR.set_ylabel('Re'); axR.set_title('Reynolds number')

for a in axes:
    a.grid(True); a.legend()

axR.set_xlabel('Time (s)')          # requirement 5

# ── animation update ─────────────────────────────────────────────────────────
start_t = time.perf_counter()
def update(_):
    # read Uno
    if not ser1.in_waiting or not ser2.in_waiting:
        return []
    try:
        T1, P1 = map(float, ser1.readline().decode().strip().split(','))
        T2, P2 = map(float, ser2.readline().decode().strip().split(','))
    except ValueError:
        return []

    # smooth
    T1 = smooth(T1_raw, T1); P1 = smooth(P1_raw, P1)
    T2 = smooth(T2_raw, T2); P2 = smooth(P2_raw, P2)

    # derived
    rho = 0.5*(P1/(R_AIR*(T1+273.15)) + P2/(R_AIR*(T2+273.15)))
    dP  = P1 - P2
    U   = math.sqrt(2*dP/rho) if dP > 0 else 0
    E   = dP / rho if rho else 0
    Re  = rho*U*CHORD/MU_AIR if U else 0

    # time axis (seconds since start)
    t = time.perf_counter() - start_t

    # buffers
    t_buf.append(t)
    T1_buf.append(T1); P1_buf.append(P1)
    T2_buf.append(T2); P2_buf.append(P2)
    dP_buf.append(dP); U_buf.append(U)
    E_buf.append(E);   Re_buf.append(Re)

    # log CSV
    if LOG_TO_CSV:
        writer.writerow([f'{t:.1f}',T1,P1,T2,P2,dP,U,E,Re]); csv_f.flush()

    # update plot data
    l_T1.set_data(t_buf, T1_buf); l_T2.set_data(t_buf, T2_buf)
    l_P1.set_data(t_buf, P1_buf); l_P2.set_data(t_buf, P2_buf)
    l_dP.set_data(t_buf, dP_buf); l_U .set_data(t_buf, U_buf); l_E.set_data(t_buf, E_buf)
    l_Re.set_data(t_buf, Re_buf)

    # rescale axes
    for a in axes:
        a.relim(); a.autoscale_view()

    # custom x ticks every 5 s (requirement 5)
    if t_buf:
        xmax = t_buf[-1]
        axR.set_xticks(np.arange(0, xmax+XTICK_SPACING_S, XTICK_SPACING_S))

    # expand Re y-axis a little (requirement 6)
    if Re_buf:
        ymin, ymax = min(Re_buf), max(Re_buf)
        pad = (ymax - ymin) * (RE_Y_EXPAND - 1)
        axR.set_ylim(ymin - pad, ymax + pad)

    return l_T1,l_T2,l_P1,l_P2,l_dP,l_U,l_E,l_Re

ani = animation.FuncAnimation(fig, update,
                              interval=1_000//SAMPLE_HZ, blit=False)

plt.tight_layout()
plt.show()

# cleanup
ser1.close(); ser2.close()
if LOG_TO_CSV: csv_f.close()
