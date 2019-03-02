import threading

from entities.enums.robot_commands import ROBOT_COMMANDS
from entities.enums.motor_names import MOTOR_NAMES

class RobotController(object):
  def __init__(self, robot, command_listener):
    self.robot = robot
    self.command_listener = command_listener
  
  def start(self):
    self.command_listener.on(ROBOT_COMMANDS["SET_SPEED"], self.handle_set_speed)
    self.start_status_reporter()

  def start_status_reporter(self):
    self.send_status()
    threading.Timer(1, self.start_status_reporter).start()
  
  def send_status(self):
    print(self.robot.get_status())

  def handle_set_speed(self, data):
    motor = data["motor"]
    speed = data["speed"]
    if (motor == MOTOR_NAMES["LEFT"]):
      self.robot.left_motor.set_speed(speed)
    elif (motor == MOTOR_NAMES["RIGHT"]):
      self.robot.right_motor.set_speed(speed)
