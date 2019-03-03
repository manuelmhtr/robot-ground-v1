class PololuG2VoltageSensor(object):
  def __init__(self, pololu_g2_motor_controllers):
    self.motor_controllers = pololu_g2_motor_controllers

  def get_voltage(self):
    voltages = []
    for motor_controller in self.motor_controllers:
      voltages.append(motor_controller.get_voltage())
    return sum(voltages) / len(voltages)
