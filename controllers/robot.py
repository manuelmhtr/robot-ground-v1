from entities.enums.robot_commands import ROBOT_COMMANDS
from entities.enums.motor_names import MOTOR_NAMES

class RobotController(object):
  def __init__(self, params):
    self.command_listener = params["command_listener"]
    self.right_motor_controller = params["right_motor_controller"]
    self.left_motor_controller = params["left_motor_controller"]
  
  def start(self):
    self.command_listener.on(ROBOT_COMMANDS["SET_SPEED"], self.handle_set_speed)

  def handle_set_speed(self, data):
    motor = data["motor"]
    speed = data["speed"]
    if (motor == MOTOR_NAMES["RIGHT"]):
      self.right_motor_controller.set_speed(speed)
    elif (motor == MOTOR_NAMES["LEFT"]):
      self.left_motor_controller.set_speed(speed)
