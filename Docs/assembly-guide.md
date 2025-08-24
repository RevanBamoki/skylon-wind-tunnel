# Skylon V1 – Assembly Guide

Instructions for assembling the **Skylon V1 desktop wind tunnel**.

---

## 1. Adhesives and General Notes

- PLA parts are joined using **superglue with activator spray**.  
- Before gluing, **dry-fit all parts** to ensure proper alignment.  
- For parts that include magnets, carefully **check polarity before securing** (see Section 3).  
- This V1 prototype was built quickly and simply. Some shortcuts (like gluing the motor) are not recommended for long-term reliability but are documented here for transparency.  

---

## 2. Structural Assembly

1. Print and prepare all STL parts (see [STL/README.md](../STL) for recommended print order).  
2. Bond the tunnel parts in sequence:  
   - **Bellmouth sections → Test section → Exit diffuser → Tunnel Supports**  
3. Ensure all joints are square and aligned to avoid air leakage.  

---

## 3. Magnet Installation (Critical Step)

- **Magnets required:** 8 total  
  - 4 in the **test section**  
  - 4 in the **magnet lid**  
- Place magnets into their slots.  
- **Check polarity before gluing**: magnets must attract, not repel.  
- Once polarity is correct, secure with superglue.  

**Warning:** If glued incorrectly, parts cannot be salvaged; you will need to reprint.  

---

## 4. Motor and Turbine

- Motor sits inside the **3D-printed motor case**.  
- For V1, the motor was **superglued** into the case (fasteners not included).  
- Attach the turbine to the motor shaft:  
  - In V1, a **custom 3D-printed adapter** was used to connect the motor shaft and turbine.  
  - Design your own adapter depending on your motor type.  
- Wires with crocodile clips connect to the motor leads and exit through the diffuser section and connect to a **DC power supply**.  

**Note:** A standalone DC motor with custom turbine was chosen instead of a PC fan, since suitable fans were more expensive and provided weaker suction.  

---

## 5. Laser & Flow Visualization

- A **green laser pointer** was used.  
- Since the beam does not naturally scatter, a **triangular prism** was glued in place to create a **laser sheet**.  
- The laser sheet illuminates smoke from incense sticks in the test section, allowing laminar/turbulent visualization.  

---

## 6. Smoke Source

- **Incense sticks** are used for smoke generation.  
- Place a **wet paper towel** beneath the sticks to catch falling ash and prevent surface damage.  

---

## 7. Sensor Installation

- Two **BMP180 pressure/temperature sensors** were mounted beneath the tunnel.
- Slots for sensors were manually drilled into the bottom of the PLA (However, if you take dimensions and have holes in your design, it's way more convenient). 
  - Ensure enough clearance for the modules and their 4-wire connections.  
  - A **rectangular slot** is recommended.  
- Sensors connect to Arduino boards as described in [Electronics/Firmware](../Electronics).  

---

## 8. Power & Wiring

- Motor connected to an **external DC power supply**.  
- Sensors wired to **Arduino Nano & Uno** (see [Electronics/Firmware](../Electronics)), which connect to a laptop via USB.  
- Data is logged and processed using the Python script in [Software/Python/bmp180_logger.py](../Software).  

---

## 9. Final Notes

- This V1 prototype is a **proof of concept**, not optimized for durability or production.  
- Future versions should:  
  - Replace glued joints with **screws/fasteners**  
  - Add **dedicated sensor mounts**  
  - Redesign the motor housing for easier serviceability  
- Despite its limitations, this prototype is functional and capable of producing meaningful airflow visualization.  

