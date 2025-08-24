# **Skylon V1 – Assembly Guide**





### **1. Adhesives and General Notes**



PLA parts are joined using superglue with activator spray.



Before gluing, dry-fit all parts to ensure proper alignment.



For parts that include magnets, carefully check polarity before securing (see Section 3).



This V1 prototype was built quickly and simply. Some shortcuts (like gluing the motor) are not recommended for long-term reliability but documented here for transparency.





### **2. Structural Assembly**



Print and prepare all STL parts (see STL/README.txt for recommended print order).



Bond the tunnel parts in sequence: bellmouth sections → test section → exit diffuser → supports.



Ensure all joints are square and aligned to avoid air leakage.





### **3. Magnet Installation (Critical Step)**



Magnets: 4 in the test section, 4 in the magnet lid (8 total).



Place magnets into their slots. Check polarity before gluing; the magnets must attract, not repel.



Once polarity is correct, secure with superglue.



**Warning:** If glued incorrectly, parts cannot be salvaged; you’ll need to reprint.





### **4. Motor and Turbine**



Motor sits inside the 3D-printed motor case.



For V1, motor was superglued into the case (fasteners not included).



Attach the turbine to the motor shaft (here I designed and 3D printed a custom adapter to fit my motor's shaft and the turbine. Design yours corresponding to what kind of motor you have.)



Wires exit through the diffuser section and connect to a DC power supply using crocodile clips.



Reason: a standalone DC motor with custom turbine was chosen instead of a PC fan, since suitable fans were expensive and less powerful for suction.





### **5. Laser \& Flow Visualization**



A green laser pointer was used.



Since it doesn’t naturally scatter, a triangular prism was glued into place to create a laser sheet.



Laser illuminates smoke from incense sticks in the test section, allowing laminar/turbulent visualization.





### **6. Smoke Source**



Incense sticks are used for smoke generation.



Place a wet paper towel beneath the sticks to catch falling ash and prevent damage to surfaces.





### **7. Sensor Installation**



Two BMP180 pressure/temperature sensors were mounted under the tunnel.



Slots for sensors were manually drilled into the bottom of the PLA. Ensure enough clearance for the sensor modules and their 4 wires each (rectangular hole recommended).



Sensors connect to Arduino boards as described in Electronics/Firmware.





### **8. Power \& Wiring**



Motor connected to external DC power supply.



Sensors wired to Arduino Nano \& Uno (see Electronics/Firmware), which were connected to my laptop via USB cables.



Data logged and processed via Python script in Software/Python/bmp180\_logger.py.





### **9. Final Notes**



This V1 prototype is a proof of concept. It's not optimized for durability or production.



Future versions should replace glued joints with screws/fasteners, add proper sensor mounts, and redesign motor housing for serviceability.



Despite limitations, this prototype is functional and capable of producing meaningful airflow visualization.

