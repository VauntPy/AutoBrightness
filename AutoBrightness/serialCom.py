#Using BH1750 sensor
import subprocess
import serial

class SerialConn:
    def __init__(self, bRate: int, port: str):
        self.bRate = bRate
        self.port = port
        self.ser = serial.Serial()

    def setConn(self):
        try: 
            self.ser.baudrate = self.bRate
            self.ser.port = self.port
            self.ser.open()
        except serial.SerialException:
            print(f"Couldn't connect to Port {self.port}")

    def closeConn(self):
        self.ser.close()
        print(f'Port {self.port} Closed')

    @staticmethod
    def listPorts():
        sp = subprocess.run('python -m serial.tools.list_ports')
        return sp


# sc = SerialConn(19200, 'COM1')
# SerialConn.listPorts()



