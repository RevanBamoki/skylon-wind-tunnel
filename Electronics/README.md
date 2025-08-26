# Electronics - Firmware

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

## Wiring

For both Uno and Nano:

- **BMP180 VCC → 5V**  
- **BMP180 GND → GND**  
- **BMP180 SDA → A4**  
- **BMP180 SCL → A5**  

---

## Libraries

Install via **Arduino IDE Library Manager**:

- **Adafruit BMP085 Library** (automatically pulls **Adafruit BusIO** and **Adafruit Unified Sensor**)  
- **Wire** (built-in)

---

## Uploading

1. Connect board via USB.  
2. Select the correct **board type** (Uno or Nano) and **COM port** in Arduino IDE.  
3. Open the corresponding sketch and click **Upload**.  
4. Close the Arduino IDE’s Serial Monitor before running the Python dashboard.  
