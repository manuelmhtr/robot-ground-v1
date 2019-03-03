from entities.models.component import Component

class Motor(Component):
  def __init__(self, motor_controller):
    super().__init__()
    self.motor_controller = motor_controller
    self.set_speed(0)

  def set_speed(self, speed):
    print('motor set speed')
    self.motor_controller.set_speed(speed)
    self.report_change()

  def get_status(self):
    return {
      "speed": self.motor_controller.get_speed()
    }
