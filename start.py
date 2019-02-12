from infrastructure.config import get_robot_id, get_usb_port_name, get_right_motor_config, get_left_motor_config
from infrastructure.motor_controllers.pololu_g2 import PololuG2MotorController
from infrastructure.command_listeners.pubnub import PubnubCommandListener
from controllers.robot import RobotController

def start_robot():
  controller = RobotController({
    "command_listener": PubnubCommandListener(get_robot_id()),
    "right_motor_controller": get_right_motor_controller(),
    "left_motor_controller": get_left_motor_controller()
  })
  controller.start()

def get_right_motor_controller():
  usb_port_name = get_usb_port_name()
  motor_config = get_right_motor_config()
  device_number = motor_config["device_number"]
  return PololuG2MotorController(usb_port_name, device_number)

def get_left_motor_controller():
  usb_port_name = get_usb_port_name()
  motor_config = get_left_motor_config()
  device_number = motor_config["device_number"]
  return PololuG2MotorController(usb_port_name, device_number)

start_robot()
