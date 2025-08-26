# Bill of Materials (BOM)

List of required components for building **Skylon V1** wind tunnel.  

---

## Components

| Item                                    | Qty   | Notes                                                                 | Purchase Link | Est. price (USD) |
|-----------------------------------------|-------|----------------------------------------------------------------------|---------------|------------------|
| Arduino Uno R3                          | 1     | Compatible microcontroller board                                     | [Amazon – Uno R3](https://www.amazon.com/WWZMDiB-ATmega328P-microcontroller-Development-Compatible/dp/B0BV9XFQ5T/) | $6.99 |
| Arduino Nano V3.0 (ATmega328P)          | 1     | Compact microcontroller board                                        | [Amazon – Nano V3.0 (2-pack)](https://www.amazon.com/LUIRSAY-2Pcs-ATmega328P-Microcontroller-Compatible/dp/B0F1FQMNXM/) | $9.99 (2 pcs) |
| BMP180 Barometric Sensor Module         | 2     | I²C pressure/temperature breakout                                    | [Amazon – BMP180 (6-pack)](https://www.amazon.com/ACEIRMC-Temperature-Barometric-Pressure-Arduino/dp/B091GWXM8D/) | $6.99 (6 pcs) |
| RS-385 12 V Brushed DC Motor            | 1     | Suction blower motor; users may adapt CAD for motor case/shaft size  | [AliExpress – RS385 Motor](https://www.aliexpress.com/i/2251832829763932.html) | $2.03 |
| 532 nm Green Laser Pointer              | 1     | Forms laser sheet with prism                                         | [Amazon – Green Laser Pointer](https://www.amazon.com/Advanced-Long-Range-Laser-Pointer-Power/dp/B0DP9G71M2/) | $8.53 |
| BK7 Triangular Glass Prism (25 mm base) | 1     | Fanning laser into sheet; adjust CAD holder to prism height          | [eBay – BK7 Triangular Prism](https://www.ebay.com/itm/304094073131) | $7.51 |
| Rectangular Neodymium Magnets (20×6×1.5 mm, N42) | 8 | For test section lid; replace CAD slot sizes as needed | [First4Magnets – 20×6×1.5 mm](https://www.first4magnets.com/product/20-x-6-x-15mm-thick-n42-neodymium-magnet-16kg-pull-19331) | ~ £5.19 / pack |
| PLA Filament (1.75 mm, 1 kg spool)      | ~1    | For all 3D-printed parts                                             | [Amazon – Overture PLA](https://www.amazon.com/OVERTURE-Filament-Consumables-Dimensional-Accuracy/dp/B07PGY2JP1/) | $14.99 |
| Acrylic Sheet, clear 6 mm               | 1     | Window; order ≥90×90 mm and cut to size                             | [Sheet Plastics – 6 mm Clear](https://www.sheetplastics.co.uk/clear-acrylic/6mm-clear-acrylic-sheet-cut-to-size#/) | ~ £1–2 (size-dependent) |
| Incense Sticks                          | –     | For smoke visualization of airflow                                   | [Amazon – HEM Incense (120 pcs)](https://www.amazon.com/Hem-Lavender-Incense-Sticks-Count/dp/B0021GBNPC/) | $6.90 |
| Adjustable DC Bench Supply (0–30 V, 5 A)| 1     | For motor speed control; crocodile clips included                    | [Amazon – WEP DC Power Supply](https://www.amazon.com/Adjustable-Switching-Regulated-Precision-Adjustments/dp/B0BN1F6CGZ/) | $49.99 |

---

**Estimated prototype total:** **~$155–165** (parts only; varies by supplier and shipping).  

### Notes
- The **motor** is RS-385-class brushed DC; other small brushed DC motors can be used if the CAD is adapted for case/shaft size.  
- The **magnets** in my prototype were **oval (obround) slot magnets**, but these are not ideal and hard to source. Rectangular magnets (like the First4Magnets link) are better and more readily available. You can edit the CAD slot dimensions to match whatever magnet size you purchase (smaller sizes are fine).  
- The **BK7 prism** (25 mm × ~80 mm) matches your build, but any equilateral prism works if you adjust the holder CAD.  
- Acrylic sheet is cut-to-size; just ensure at least 90 × 90 mm and trim if needed. Or if you want a smaller size than the one I used, just make sure to update the test section rectangular.  
- **Microcontrollers:** You don’t strictly need both an Uno and a Nano. You could use two Unos or two Nanos - sensor performance isn’t affected. The reason for two boards is that the BMP180 sensors both use the same fixed I²C address (0x77), so a single microcontroller cannot distinguish them on the same bus. Splitting them across two boards is the simplest solution.  
- Buying multipacks (Nano, BMP180) reduces cost but leaves spares for contributors.  
