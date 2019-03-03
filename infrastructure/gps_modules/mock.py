import random

class MockGPSModule(object):
  DEFAULT_LATITUDE = 20.694811666666666
  DEFAULT_LONGITUDE = -103.38541333333333
  RANDOM_RANGE=0.0001

  def __init__(self):
    self.latitude = None
    self.longitude = None

  def get_location(self):
    self.latitude = self.DEFAULT_LATITUDE + random.uniform(-self.RANDOM_RANGE, self.RANDOM_RANGE)
    self.longitude = self.DEFAULT_LONGITUDE + random.uniform(-self.RANDOM_RANGE, self.RANDOM_RANGE)
    return {
      "latitude": self.latitude,
      "longitude": self.longitude
    }
