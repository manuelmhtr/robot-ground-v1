class Battery(object):
  def __init__(self, voltage_sensor):
    self.voltage_sensor = voltage_sensor
  
  def get_status(self):
    return {
      "voltage": self.voltage_sensor.get_voltage()
    }
