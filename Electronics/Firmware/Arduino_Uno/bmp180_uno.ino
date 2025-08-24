#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  if (!bmp.begin()) {
    Serial.println("Sensor 1 not found!");
    while (1);
  }
}


void loop() {
  float T1 = bmp.readTemperature(); 
  float P1 = bmp.readPressure();

  Serial.print(T1, 2); Serial.print(',');   // match Nano’s 5 Hz rate
  Serial.println(P1, 0);

  delay(50);
}
