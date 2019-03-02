import time
import serial
import pynmea2
import threading

class SixfabGPSModule(object):
  PORT_NAME = '/dev/ttyUSB1'
  BAUDRATE = 9600

  def __init__(self):
    self.latitude = None
    self.longitude = None
    self.serial_client = get_serial_client(self.PORT_NAME, self.BAUDRATE)
    self.start_gps_tracking()

  def get_location(self):
    return {
      "latitude": self.latitude,
      "longitude": self.longitude
    }

  def start_gps_tracking(self):
    self.serial_client.open()
    thread = threading.Thread(target=self.read_serial_port, args=())
    thread.daemon = True
    thread.start()

  def read_serial_port(self):
    while True:
      if self.serial_client.inWaiting() > 0:
        raw = self.serial_client.readline().decode("utf-8")

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
