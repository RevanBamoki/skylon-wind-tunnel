# Testing Procedures (Skylon V1 - Prototype)

Procedures for verifying assembly, sensor operation, and visualization on the **Skylon V1 desktop wind tunnel**.

---

## 1. Leak & Fit Check

- Feel for leaks around glue joints.  
- Re-glue if any clear leaks are detected.  

---

## 2. Sensor Check (Room Conditions)

- Power each Arduino via USB.  
- Open Serial Monitor (9600 baud) **one at a time**.  
- Confirm readings:  
  - **T1/T2** ≈ room temperature  
  - **P1/P2** ≈ ambient (≈100–103 kPa)  
- Close Serial Monitor when finished.  

---

## 3. Dual-Stream Readout

- Run:  
  ```bash
  python Software/Python/bmp180_logger.py
  ```  
  (with the correct `UNO_PORT` and `NANO_PORT` set in the script).  
- You should see live plots for:  
  - T1, T2  
  - P1, P2  
  - ΔP  
  - U (airflow velocity)  
  - E_loss  
  - Re (Reynolds number)  
- **Note:** Values are *indicative only* (prototype, uncalibrated).  

---

## 4. Flow Visualization

- Place incense upstream.  
- Turn on the **laser + prism** to form a sheet.  
- Observe flow patterns at the model.  

---

## 5. Basic Sanity Ranges (Informal)

- ΔP should be **positive** when suction is on.  
- U should **increase with motor voltage**.  
- Re should **increase with U (monotonic trend)**.  
- Absolute values may not be accurate at prototype stage.  

---

## 6. Data Logging

- Enable logging by setting:  
  ```python
  LOG_TO_CSV = True
  ```  
- Inspect results in:  
  ```
  bmp_dual_log.csv
  ```  

---

## Safety

- **Laser:** Avoid direct or reflective eye exposure. Always use protective eyewear.  
- **Incense:** Ensure good ventilation. Place a damp paper towel beneath sticks to catch ash.  
- **Hot components/adhesives:** Handle with care during extended operation.  
