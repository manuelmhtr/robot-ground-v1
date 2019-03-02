class GPS(object):
  def __init__(self, gps_module):
    self.gps_module = gps_module
  
  def get_status(self):
    location = self.gps_module.get_location()
    return {
      "latitude": location["latitude"],
      "longitude": location["longitude"]
    }
