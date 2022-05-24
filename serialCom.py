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
            print(self.ser.is_open)
        except serial.SerialException:
            print(f"Couldn't connect to Port {self.port}")

    def readBytes(self, numBytes):
        return self.ser.read(numBytes)

    def sendBytes(self):
        self.ser.write(b'Connection')

    def closeConn(self):
        self.ser.close()
        print(f'Port {self.port} Closed')

    @staticmethod
    def listPorts():
        sp = subprocess.run('python -m serial.tools.list_ports', stdout=subprocess.PIPE)
        return sp.stdout.decode().rstrip().split()




# n = SerialConn.listPorts()
# sec = SerialConn(19200, n[0])
# sec.setConn()
# sec.sendBytes()
# d = sec.readBytes(8)
# print(d)


# b = sec.readBytes(8)
# b = b.decode()
# print(b)
# print(type(b))


