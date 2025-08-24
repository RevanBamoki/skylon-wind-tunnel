#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  if (!bmp.begin()) {
    Serial.println("Sensor 2 not found!");
    while (1);
  }
}


void loop() {
  float T2 = bmp.readTemperature();      // °C
  float P2 = bmp.readPressure();         // Pa

  Serial.print(T2, 2);   Serial.print(',');   // <-- 5 Hz instead of 1 Hz
  Serial.println(P2, 0);                  

  delay(50);                             // 0.2 s ≈ 5 samples s-1
}
