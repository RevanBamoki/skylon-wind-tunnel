# Skylon V1 — Open-Source Desktop Wind Tunnel  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)  
![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-orange.svg)  
![Status: Prototype](https://img.shields.io/badge/status-prototype-yellow.svg)  

A compact, 3D-printed wind tunnel you can build for classrooms, clubs, or hobby labs.  

---

## Repository Structure
- **STL/** – 3D-printable parts + print order & PLA settings  
- **CAD/** – Fusion 360 source (`.f3z`) and STEP export  
- **Electronics/** – Arduino firmware for dual BMP180 sensors (Uno + Nano)  
- **Software/** – Python live dashboard + CSV logger  
- **Docs/** – Assembly guide, testing procedures  
- **BOM/** – Bill of Materials  

---

## Quick Start
1. Print parts per **STL/README.md** (check magnet polarity note).  
2. Assemble per **Docs/assembly-guide.md**.  
3. Flash **Electronics/Firmware/** to:  
   - Uno → pressure P1, temperature T1  
   - Nano → pressure P2, temperature T2  
4. Run **Software/Python/bmp180_logger.py** (see its README for dependencies + COM port settings).  
5. Visualize flow. Data are *indicative only* (prototype, uncalibrated).  

---

## License & Disclaimer  
📜 Licensed under the **MIT License**.  
⚠️ **Prototype status:** results are for educational/demo purposes only.  

---

