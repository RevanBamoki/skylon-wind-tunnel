# Software — Live Dashboard & Logger

Python tools to visualize and log data from the dual-BMP180 sensor setup inside the **Skylon V1** wind tunnel.

---

## Overview
This package connects to two Arduino boards:

- **Arduino Uno** → T1 (temperature) + P1 (pressure)  
- **Arduino Nano** → T2 (temperature) + P2 (pressure)

The Arduino sketches are included in [`Electronics/Firmware`](../Electronics).

After flashing the boards, close the Arduino IDE’s serial monitor and run the Python program.

The logger will:
- Stream live data from both sensors via serial.  
- Compute derived flow quantities in real time:  
  - Pressure difference (ΔP)  
  - Airflow velocity (U)  
  - Energy loss per unit mass (E_loss)  
  - Reynolds number (Re)  
- Display four live plots.  
- Optionally log all data to a CSV file.

---

## Requirements

- **Python**: 3.8 or newer  
- **Pip packages**:
  ```bash
  pip install pyserial matplotlib numpy
Standard library modules (already included): csv, time, math, collections

Usage
Upload the Arduino sketches (Arduino_Uno and Arduino_Nano) to their boards.

Close the Arduino IDE’s serial monitor.

Edit the top of bmp180_logger.py if needed:

python
Copy
Edit
UNO_PORT   = "COM5"     # or /dev/ttyUSB0
NANO_PORT  = "COM4"     # or /dev/ttyUSB1
CSV_FILE   = "bmp_dual_log.csv"
LOG_TO_CSV = True       # set False to disable logging
Run the script:

bash
Copy
Edit
python bmp180_logger.py
Live plots will appear, and (if enabled) data will be saved to CSV.

Example Output
Temperature plot → T1 (Uno) vs T2 (Nano)

Pressure plot → P1 vs P2

ΔP/U/E_loss plot → flow dynamics

Reynolds number plot → indicates flow regime

Notes
Default sampling frequency = 20 Hz (SAMPLE_HZ).

Plots auto-rescale but can be tuned (HISTORY_SAMPLES, XTICK_SPACING_S).

Assumes BMP180 sensors, but adaptable for similar pressure/temperature sensors.

If you hit serial errors:

Windows → check Device Manager for COM port

Linux/Mac → use /dev/ttyUSB*

Repository Navigation
Electronics → Arduino firmware

Software → this Python dashboard/logger

Docs → Assembly guide & calibration notes