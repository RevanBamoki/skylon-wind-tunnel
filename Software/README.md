# **Software – Live Dashboard \& Logger**



This folder contains the Python software used to visualize and log data from the dual-BMP180 sensor setup inside the Skylon V1 wind tunnel.





### **Overview**



The script (bmp180\_logger.py) connects to two Arduino boards:



* **Arduino Uno** – reads T1 (temperature) and P1 (pressure).



* **Arduino Nano** – reads T2 and P2.



The Arduino sketches for each board are included in Electronics/Firmware.



After uploading those to your Uno and Nano, close the Arduino IDE’s serial monitor and then run this Python program.



The program will:



* Stream live data from both sensors via serial.



* Compute derived quantities in real time:



Pressure difference (ΔP)



Airflow velocity (U)



Energy loss per unit mass (E\_loss)



Reynolds number (Re)



* Display four live plots (temperature, pressure, ΔP/U/E\_loss, Reynolds number).



* Optionally log all data to a CSV file.





### **Requirements**



###### **Python version**



* Python 3.8 or newer is recommended.



###### **Required packages**



Install the following with pip:



pip install pyserial matplotlib numpy



###### **Standard library modules (already included in Python)**



* csv, time, math, collections





### **Usage**



1. Upload the Arduino sketches (Electronics/Firmware/Arduino\_Uno and Arduino\_Nano) to their respective boards.



2\. Close the Arduino IDE’s serial monitor so the ports are free.



3\. Edit the top of the Python script (bmp180\_logger.py) if needed:



* UNO\_PORT – e.g., COM5 (Windows) or /dev/ttyUSB0 (Linux/Mac).



* NANO\_PORT – e.g., COM4 or /dev/ttyUSB1.



* CSV\_FILE – filename for CSV logging.



* LOG\_TO\_CSV = True/False – toggle logging.



4\. Run the script:



python bmp180\_logger.py



5\. Four plots will appear and update live. Data is simultaneously saved to bmp\_dual\_log.csv if logging is enabled.





### **Example Output**



* Temperature plot: T1 (Uno) vs T2 (Nano)



* Pressure plot: P1 vs P2



* ΔP/U/E\_loss plot: visualizes flow dynamics



* Reynolds number plot: indicates flow regime





### **Notes**



* Sampling frequency is set to 20 Hz (SAMPLE\_HZ variable).



* Plots auto-rescale but can be tuned in the script (HISTORY\_SAMPLES, XTICK\_SPACING\_S, etc.).



* The script assumes BMP180 sensors but can be adapted for similar pressure/temperature sensors.



* If serial connections fail, check your Arduino ports in Device Manager (Windows) or ls /dev/ttyUSB\* (Linux).
