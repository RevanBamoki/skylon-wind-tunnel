# **Testing Procedures (Skylon V1 — Prototype)**



###### **1) Leak \& fit check**

\- Tape off open ends, gently pressurize by hand (or a fan) and feel for leaks around glue joints.

\- Re-glue if you feel clear leaks.





###### **2) Sensor check (room conditions)**

\- Power each Arduino via USB; open Serial Monitor (9600 baud) one at a time.

\- Confirm T1/T2 read ~room temp and P1/P2 ~ambient (≈100–103 kPa). Close Serial Monitor when done.





###### **3) Dual‑stream readout**

\- Run `Software/Python/bmp180\_logger.py` with the correct `UNO\_PORT` and `NANO\_PORT`.

\- You should see live plots for T1/T2, P1/P2, ΔP, U, E\_loss, Re.

\- Note: values are \*\*indicative\*\* (prototype, uncalibrated).





###### **4) Flow visualization**

\- Place incense upstream; turn on laser + prism to form a sheet.

\- Observe laminar vs turbulent patterns at the model.





###### **5) Basic sanity ranges (informal)**

\- ΔP positive when suction is on.

\- U increases with motor voltage.

\- Re increases with U (monotonic). Absolute values may not be accurate.





###### **6) Data logging**

\- Toggle `LOG\_TO\_CSV = True`; inspect `bmp\_dual\_log.csv` in your editor.





###### **Safety**

\- Laser: avoid direct/reflective eye exposure; use appropriate eyewear.

\- Incense: ventilate; place a damp paper towel under ash.

\- Hot components/adhesives: handle with care.



