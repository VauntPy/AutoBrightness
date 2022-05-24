import screen_brightness_control as sbc
import requests

# url = f"https://{SERVER}/external/api/get?token={TOKEN}&{VIRTUAL-PIN}"

class Screen:
    def __init__(self, token, vPin) -> None:
        self.url = f"https://blynk.cloud/external/api/get?token={token}&{vPin}"
        self.pVal = "0"
    def setBrightness(self):
        self.cVal = self.getExternalLight()
        if self.cVal != self.pVal: 
            sbc.set_brightness(self.cVal)
            self.pVal = self.cVal
            print(f"Setting Brightness to {self.pVal} %")     
    def getExternalLight(self):
        return requests.get(self.url).text 
    @staticmethod
    def getBrightness():
        return sbc.get_brightness()



