class PololuG2VoltageSensor(object):
  def __init__(self, pololu_g2_motor_controller):
    self.motor_controller = pololu_g2_motor_controller

  def get_voltage(self):
    return "default voltage"
