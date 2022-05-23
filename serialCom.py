import subprocess
import serial
import time

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
            # print(self.ser.isOpen())
        except serial.SerialException:
            print(f"Couldn't connect to Port {self.port}")

    def closeConn(self):
        self.ser.close()
        print(f'Port {self.port} Closed')

    @staticmethod
    def listPorts():
        sp = subprocess.run('python -m serial.tools.list_ports', stdout=subprocess.PIPE)
        return sp.stdout.decode().rstrip().split()




n = SerialConn.listPorts()
# print(n)




