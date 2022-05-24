/* Comment this out to disable prints and save space */
#define BLYNK_PRINT Serial

/* Fill-in your Template ID (only if using Blynk.Cloud) */
//#define BLYNK_TEMPLATE_ID   "YourTemplateID"
// #define BUILT_IN_LED 33

#include <BlynkSimpleEsp32.h>
#include <WiFiClient.h>
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

void myTimerEvent()
{
  // You can send any value at any time.
  // Please don't send more that 10 values per second.
  int rVal = random(0, 101);
  Blynk.virtualWrite(V1, rVal);

}

void WiFiStationDisconnected(WiFiEvent_t event, WiFiEventInfo_t info){
  Blynk.connect();
}

void setup()
{
  // Debug console
  // pinMode(BUILT_IN_LED, OUTPUT);
  WiFi.onEvent(WiFiStationDisconnected, SYSTEM_EVENT_STA_DISCONNECTED);
  timer.setInterval(5000L, myTimerEvent);
  
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
