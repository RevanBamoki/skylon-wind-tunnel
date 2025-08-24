[Uploading README.md…]()
# Skylon V1: Open-Source Desktop Wind Tunnel

![TunnelPhoto](https://github.com/user-attachments/assets/503b3e37-8a9f-4ccd-8122-8aeb38351430)


[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/release/python-380/)  
[![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-orange.svg)](https://www.arduino.cc/en/software)  
[![Status: Prototype](https://img.shields.io/badge/status-prototype-yellow.svg)]()

A compact, 3D-printed wind tunnel you can build for classrooms, hobby and university labs.

---

## Repository Structure

- **STL/** - 3D-printable parts + print order & PLA settings  
- **CAD/** - Fusion 360 source (`.f3z`) and STEP export  
- **Electronics/** - Arduino firmware for dual BMP180 sensors (Uno + Nano)  
- **Software/** - Python live dashboard 
- **Docs/** - Assembly guide, and testing procedures  
- **BOM/** - Bill of Materials  

---

## Quick Start

1. Print parts per **STL/README.md**.  
2. Assemble per **Docs/assembly-guide.md**.  
3. Flash **Electronics/Firmware/** to:  
   - Uno → pressure P1, temperature T1  
   - Nano → pressure P2, temperature T2  
4. Per the steps in **Docs\testing-procedures.md**, run **Software/Python/bmp180_logger.py** (see its README for dependencies). 
5. Visualize flow. Data are *indicative only* (prototype, uncalibrated).  

---

## License & Disclaimer

- Licensed under the **MIT License**.  
- **Prototype status:** Results are for educational/demo purposes only.  

---
