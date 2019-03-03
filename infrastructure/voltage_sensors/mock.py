import random

class MockVoltageSensor(object):
  def __init__(self):
    self.voltage = random.uniform(6.6, 8.4)

  def get_voltage(self):
    return self.voltage
