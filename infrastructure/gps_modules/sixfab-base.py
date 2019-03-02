import time
import serial
import pynmea2
import threading

class SixfabBaseGPSModule(object):
  WRITE_PORT_NAME = '/dev/ttyUSB2'
  READ_PORT_NAME = '/dev/ttyUSB1'
  BAUDRATE = 115200
  TIMEOUT = 1

  def __init__(self):
    self.latitude = None
    self.longitude = None
    self.write_serial_client = serial.Serial(self.WRITE_PORT_NAME, baudrate = self.BAUDRATE, timeout = self.TIMEOUT)
    self.read_serial_client = serial.Serial(self.READ_PORT_NAME, baudrate = self.BAUDRATE, timeout = self.TIMEOUT)
    self.start_gps_tracking()

  def get_location(self):
    return {
      "latitude": self.latitude,
      "longitude": self.longitude
    }

  def start_gps_tracking(self):
    self.write_serial_client.write('AT+QGPS=1\r'.encode())
    self.write_serial_client.close()
    thread = threading.Thread(target=self.read_serial_port, args=())
    thread.daemon = True
    thread.start()

  def read_serial_port(self):
    while True:
      if self.read_serial_client.inWaiting() > 0:
        raw = self.read_serial_client.readline().decode("utf-8")

        if raw.find("$GPGGA") != -1:
          data = pynmea2.parse(raw)
          self.latitude = data.latitude
          self.longitude = data.longitude
      time.sleep(0.1)

def get_serial_client(port_name, baud_rate):
  serial_client = serial.Serial()
  serial_client.port = port_name
  serial_client.baudrate = baud_rate
  serial_client.timeout = 1
  return serial_client
