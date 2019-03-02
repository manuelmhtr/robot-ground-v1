class Motor(object):
  def __init__(self, motor_controller):
    self.motor_controller = motor_controller
    self.set_speed(0)

  def set_speed(self, speed):
    print('motor set speed')
    self.motor_controller.set_speed(speed)

  def get_status(self):
    return {
      "speed": self.motor_controller.get_speed()
    }
