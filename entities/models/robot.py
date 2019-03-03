from entities.models.component import Component

class Robot(Component):
  def __init__(self, id, motors, battery, gps):
    super().__init__()
    self.id = id
    self.left_motor = motors["left"]
    self.right_motor = motors["right"]
    self.battery = battery
    self.gps = gps
    self.bind_change_listeners()

  def get_status(self):
    return {
      "id": self.id,
      "left_motor": self.left_motor.get_status(),
      "right_motor": self.right_motor.get_status(),
      "battery": self.battery.get_status(),
      "gps": self.gps.get_status()
    }

  def bind_change_listeners(self):
    self.left_motor.on_change(lambda data: self.report_change())
    self.right_motor.on_change(lambda data: self.report_change())
