// Using BH1750 sensor
#include <Arduino.h>
#include <BH1750.h>
#include <Wire.h>

#define I2C_SDA 12
#define I2C_SCL 13

BH1750 lightMeter(0x23);

void setup() {
  // put your setup code here, to run once:
  lightMeter.begin(BH1750::ONE_TIME_HIGH_RES_MODE_2);
  Wire.begin(I2C_SDA, I2C_SCL, 100000);
  Serial.begin(19200);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (lightMeter.measurementReady()) {
    float lux = lightMeter.readLightLevel();
    Serial.print(lux);
    delay(1000);
  }
}