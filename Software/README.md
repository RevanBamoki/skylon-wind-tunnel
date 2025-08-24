# Software — Live Dashboard & Logger

Python tools to visualize and log data from the dual-BMP180 sensor setup inside the wind tunnel.

---

## Overview
This package connects to two Arduino boards:

- **Arduino Uno** → T1 (temperature) + P1 (pressure)  
- **Arduino Nano** → T2 (temperature) + P2 (pressure)

The Arduino sketches are included in [`Electronics/Firmware`](../Electronics).

After flashing the boards, close the Arduino IDE’s serial monitor and run the Python program.

---

## Requirements

- **Python**: 3.8 or newer  
- **Pip packages**:  
  ```bash
  pip install pyserial matplotlib numpy
  ```
- Standard library modules (already included):  
  `csv`, `time`, `math`, `collections`

---

## Usage

1. Upload the Arduino sketches (`Arduino_Uno` and `Arduino_Nano`) to their respective boards.  
2. Close the Arduino IDE’s serial monitor so the ports are free.  
3. Edit the top of `bmp180_logger.py` if needed:  
   ```python
   UNO_PORT   = "COM5"     # or /dev/ttyUSB0
   NANO_PORT  = "COM4"     # or /dev/ttyUSB1
   CSV_FILE   = "bmp_dual_log.csv"
   LOG_TO_CSV = True       # set False to disable logging
   ```
4. Run the script:  
   ```bash
   python bmp180_logger.py
   ```
5. Four plots will appear and update live. If enabled, data will also be saved to CSV.  

---

## Example Output

- **Temperature plot**: T1 (Uno) vs T2 (Nano)  
- **Pressure plot**: P1 vs P2  
- **ΔP / U / E_loss plot**: flow dynamics  
- **Reynolds number plot**: flow regime indicator  

![PythonExampleOutput](https://github.com/user-attachments/assets/e63583f7-71ea-4385-b57e-f01756a9d9e8)

---

## Notes

- Sampling frequency is set to **20 Hz** (`SAMPLE_HZ`).  

- Plots auto-rescale but can be tuned (`HISTORY_SAMPLES`, `XTICK_SPACING_S`).
