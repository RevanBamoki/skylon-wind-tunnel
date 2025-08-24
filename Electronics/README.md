# Electronics — Firmware

Contains Arduino sketches for the **Skylon V1** wind tunnel.

---

## Boards

- **Arduino_Uno** → Handles BMP180 sensor for **P1** (pressure) and **T1** (temperature)  
- **Arduino_Nano** → Handles BMP180 sensor for **P2** (pressure) and **T2** (temperature)  

---

## Folder Structure

- **Firmware/Arduino_Uno/** → Code for Uno board  
- **Firmware/Arduino_Nano/** → Code for Nano board  

Each folder includes a sketch (`.ino`) that can be opened directly in the Arduino IDE.  

---

## Notes

- Ensure correct **COM port** selection before flashing.  
- Install the **Adafruit BMP085/BMP180 library** via Arduino IDE Library Manager.  
- After uploading, close the Arduino IDE’s serial monitor before running the Python dashboard.  
