/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

#define I2C_SDA 15
#define I2C_SCL 14
#define FLASH_LED 4

/* Fill-in your Template ID (only if using Blynk.Cloud) */
//#define BLYNK_TEMPLATE_ID   "YourTemplateID"
#define BLYNK_DEVICE_NAME "YOUR-DEVICE-NAME"
#define BLYNK_TEMPLATE_ID "YOUR-TEMPLATE-ID"

#include <BlynkSimpleEsp32.h>
#include <WiFiClient.h>
#include <BH1750.h>
#include <WiFi.h>
#include <Wire.h>

// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "YOUR-BLYNK-TOKEN-HERE";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "YOUR-WIFI-SSID-HERE";
char pass[] = "YOUR-WIFI-PASSWORD-HERE";

BlynkTimer timer;
BH1750 lightMeter(0x23);

void myTimerEvent()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  lightMeter.begin(BH1750::ONE_TIME_HIGH_RES_MODE);
  while (!lightMeter.measurementReady());
  float lux = lightMeter.readLightLevel();
  unsigned int aux = round(lux);
  Blynk.virtualWrite(V1, aux);
  Serial.println(aux);    
}

void WiFiStationDisconnected(WiFiEvent_t event, WiFiEventInfo_t info){
  Blynk.connect();
}

void setup()
{
  pinMode(FLASH_LED, OUTPUT);
  digitalWrite(FLASH_LED, LOW);
 
  // Debug console
  Wire.begin(I2C_SDA, I2C_SCL);

  WiFi.onEvent(WiFiStationDisconnected, SYSTEM_EVENT_STA_DISCONNECTED);
  timer.setInterval(5000L, myTimerEvent);
  
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  unsigned int count = 0;
  while(WiFi.status() != WL_CONNECTED){
    delay(100);
    Serial.println(count);
    count++;
    if(count >= 150) ESP.restart();
    
  }
  Blynk.config(auth);
}
  


void loop()
{
  Blynk.run();
  timer.run();
  
}

BLYNK_CONNECTED(){
  Blynk.syncAll();
}
