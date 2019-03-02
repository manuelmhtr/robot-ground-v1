import random

class MockGPSModule(object):
  DEFAULT_LATITUDE = 20.694811666666666
  DEFAULT_LONGITUDE = -103.38541333333333

  def __init__(self):
    self.latitude = None
    self.longitude = None

  def get_location(self):
    self.latitude = self.DEFAULT_LATITUDE + random.uniform(-0.000001, 0.000001)
    self.longitude = self.DEFAULT_LONGITUDE + random.uniform(-0.000001, 0.000001)
    return {
      "latitude": self.latitude,
      "longitude": self.longitude
    }
