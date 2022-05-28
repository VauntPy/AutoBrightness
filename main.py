from dotenv import load_dotenv
import interface
import time
import os

def main():
    load_dotenv()
    sb = interface.Screen(os.getenv("BLYNK_TOKEN"), "v1", "dic.txt")
    sb.populateDic()
    while True:
        sb.setBrightness()
        time.sleep(3)

if __name__ == "__main__":
    main()