/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

#define I2C_SDA 12
#define I2C_SCL 13



/* Fill-in your Template ID (only if using Blynk.Cloud) */
//#define BLYNK_TEMPLATE_ID   "YourTemplateID"
#define BLYNK_DEVICE_NAME "AutoBrightness"
#define BLYNK_TEMPLATE_ID "TMPLaC5YhdHz"

#include <BlynkSimpleEsp32.h>
#include <WiFiClient.h>
#include <BH1750.h>
#include <WiFi.h>
#include <Wire.h>



// You should get Auth Token in the Blynk App.
// Go to the Project Settings (nut icon).
char auth[] = "lzeeRNFN7QWK32ulKdgDhtPKmPN-oJhF";

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "WifiCarranza";
char pass[] = "#$#$#$#$??";

BlynkTimer timer;
BH1750 lightMeter(0x23);

void myTimerEvent()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  int rVal = random(0, 101);
  Blynk.virtualWrite(V1, rVal);

  if (lightMeter.measurementReady()) {
    float lux = lightMeter.readLightLevel();
    Blynk.virtualWrite(V2, lux);
  }
}

void WiFiStationDisconnected(WiFiEvent_t event, WiFiEventInfo_t info){
  Blynk.connect();
}

void setup()
{
  // Debug console
  lightMeter.begin(BH1750::ONE_TIME_HIGH_RES_MODE_2);
  Wire.begin(I2C_SDA, I2C_SCL, 100000);

  WiFi.onEvent(WiFiStationDisconnected, SYSTEM_EVENT_STA_DISCONNECTED);
  timer.setInterval(1000L, myTimerEvent);
  
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  uint32_t count = 0;
  while(WiFi.status() != WL_CONNECTED){
    delay(100);
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

// BLYNK_WRITE(V0){ 
//   int val = param.asInt();
//   digitalWrite(BUILT_IN_LED, val);
// }

