class Robot(object):
  def __init__(self, id, motors, battery, gps):
    self.id = id
    self.left_motor = motors["left"]
    self.right_motor = motors["right"]
    self.battery = battery
    self.gps = gps

  def get_status(self):
    return {
      "id": self.id,
      "left_motor": self.left_motor.get_status(),
      "right_motor": self.right_motor.get_status(),
      "battery": self.battery.get_status(),
      "gps": self.gps.get_status()
    }
