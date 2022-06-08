import subprocess
import serial

class SerialConn:
    aux = '1'

    def __init__(self, bRate: int, port: str, timeOut: int):
        self.bRate = bRate
        self.port = port
        self.ser = serial.Serial()
        self.timeOut = timeOut

    def setConn(self):
        try: 
            self.ser.baudrate = self.bRate
            self.ser.port = self.port
            self.ser.timeout = self.timeOut
            self.ser.open()
            if(self.ser.is_open):
                print(f"Connected to Port {self.port}")
        except serial.SerialException:
            print(f"Couldn't connect to Port {self.port}")

    def sendBytes(self):
        self.ser.write(self.aux.encode())

    def readBytes(self):
        return self.ser.readline().decode()

    def getLux(self):
        self.sendBytes()
        return self.readBytes()

    def closeConn(self):
        self.ser.close()
        print(f'Port {self.port} Closed')

    @classmethod
    def setPort(cls, bRate: int, timeOut=1):
        sp = subprocess.run('python -m serial.tools.list_ports', stdout=subprocess.PIPE)
        port = sp.stdout.decode().rstrip().split()[0]
        return cls(bRate, port, timeOut)


# sc = SerialConn.setPort(115200 , 2)
# sc.setConn()
# print(sc.getLux())
# sc.closeConn()



