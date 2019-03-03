import threading
from entities.models.component import Component

class GPS(Component):
  READ_LOCATION_INTERVAL = 1
  ITEMS_FOR_AVERAGE = 10
  ROUND_DECIMALS = 6

  def __init__(self, gps_module):
    super().__init__()
    self.gps_module = gps_module
    self.latitude = None
    self.longitude = None
    self.values = { "latitude": [], "longitude": [] }
    self.start_reading_location()

  def set_location(self, latitude, longitude):
    if self.latitude != latitude or self.longitude != longitude:
      self.latitude = latitude
      self.longitude = longitude
      super().report_change()

  def start_reading_location(self):
    self.read_location()
    threading.Timer(self.READ_LOCATION_INTERVAL, self.start_reading_location).start()

  def read_location(self):
    location = self.gps_module.get_location()
    avg_latitude = self.get_average_value("latitude", location)
    avg_longitude = self.get_average_value("longitude", location)
    self.set_location(avg_latitude, avg_longitude)

  def get_average_value(self, kind, location):
    if location[kind] != None:
      value = round(location[kind], self.ROUND_DECIMALS)
      self.values[kind].append(value)

    if len(self.values[kind]) > self.ITEMS_FOR_AVERAGE:
      self.values[kind].pop(0)

    if len(self.values[kind]) == 0:
      return None

    return sum(self.values[kind]) / len(self.values[kind])

  def get_status(self):
    return {
      "latitude": self.latitude,
      "longitude": self.longitude
    }
