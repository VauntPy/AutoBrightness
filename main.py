from dotenv import load_dotenv
import iotInterface
import serialCom
import time
import os

def main():
    load_dotenv()
    iot = iotInterface.Screen(os.getenv("BLYNK_TOKEN"), "v1", "dic.txt")
    iot.populateDic()

    sc = serialCom.SerialConn.setPort(115200, 1)
    sc.setConn()
    
    while True:
        # iot.setBrightness()
        iot.setBrightness(sc.getLux())
        time.sleep(5)

    
    

if __name__ == "__main__":
    main()



