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
char auth[] = "YOUR-TOKEN-HERE";

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

void setup()
{
  // Debug console
  // pinMode(BUILT_IN_LED, OUTPUT);
  
  timer.setInterval(5000L, myTimerEvent);
  Serial.begin(115200);

  if(!Blynk.connected()){
    Blynk.disconnect();
    delay(10000);
    Blynk.config(auth);
    Blynk.connectWiFi(ssid, pass);
    Blynk.connect(15);
  }
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

