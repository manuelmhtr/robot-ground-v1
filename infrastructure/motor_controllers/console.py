class ConsoleMotorController(object):
  def __init__(self):
    self.set_speed(0)
  
  def set_speed(self, speed):
    print('speed:', speed)
    self.speed = speed
  
  def get_speed(self):
    return self.speed
