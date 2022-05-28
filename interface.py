import screen_brightness_control as sbc
import requests

# url = f"https://{SERVER}/external/api/get?token={TOKEN}&{VIRTUAL-PIN}"

class Screen:
    pVal = "100"
    luxDic = {
        10: 50,
        40: 90,
        65: 90,
        100000: 100,
    }

    def __init__(self, token, vPin) -> None:
        self.url = f"https://blynk.cloud/external/api/get?token={token}&{vPin}"
     
    def setBrightness(self):
        self.cVal = self.getExternalLight()
        if self.cVal != self.pVal: 
            for key,value in self.luxDic.items():
                if int(self.cVal) <= key and self.getBrightness()[0] != value:
                    sbc.set_brightness(value)
                    self.pVal = self.cVal
                    print(f"Brightness: {value} %")
                    break

    def getExternalLight(self):
        return requests.get(self.url).text 
    @staticmethod
    def getBrightness():
        return sbc.get_brightness()

