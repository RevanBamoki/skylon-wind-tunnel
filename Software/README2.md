# Software – Live Dashboard & Logger

This folder contains the Python software used to visualize and log data from the dual-BMP180 sensor setup inside the Skylon V1 wind tunnel.

---

## Overview

The script (`bmp180_logger.py`) connects to two Arduino boards:

- **Arduino Uno** – reads T1 (temperature) and P1 (pressure).  
- **Arduino Nano** – reads T2 and P2.  

The Arduino sketches for each board are included in `Electronics/Firmware`.

After uploading those to your Uno and Nano, close the Arduino IDE’s serial monitor and then run this Python program.

The program will:

- Stream live data from both sensors via serial.  
- Compute derived quantities in real time:  
  - Pressure difference (ΔP)  
  - Airflow velocity (U)  
  - Energy loss per unit mass (E_loss)  
  - Reynolds number (Re)  
- Display four live plots (Temperature, Pressure, ΔP/U/E_loss, Reynolds number).  
- Optionally log all data to a CSV file.  

---

## Requirements

### Python version
- Python **3.8 or newer** is recommended.

### Required packages
Install the following with pip:

```bash
pip install pyserial matplotlib numpy
