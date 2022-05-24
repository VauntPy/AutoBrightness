from dotenv import load_dotenv
import interface
import os

def main():
    load_dotenv()
    sb = interface.Screen(os.getenv("BLYNK_TOKEN"), "v1")
    while True:
        sb.setBrightness()

if __name__ == "__main__":
    main()