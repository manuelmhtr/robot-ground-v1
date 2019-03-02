from infrastructure.config import get_robot_id, get_right_motor_config, get_left_motor_config
from infrastructure.command_listeners.pubnub import PubnubCommandListener
from infrastructure.gps_modules.sixfab import SixfabGPSModule
from infrastructure.motor_controllers.pololu_g2 import PololuG2MotorController
from infrastructure.motor_controllers.console import ConsoleMotorController
from infrastructure.voltage_sensors.pololu_g2 import PololuG2VoltageSensor
from controllers.robot import RobotController
from entities.models.battery import Battery
from entities.models.gps import GPS
from entities.models.motor import Motor
from entities.models.robot import Robot

def start_robot():
  robot = get_robot()
  command_listener = PubnubCommandListener(robot.id)
  controller = RobotController(robot, command_listener)
  controller.start()

def get_robot():
  left_motor_controller = get_left_motor_controller()
  right_motor_controller = get_right_motor_controller()

  id = get_robot_id()
  motors = get_motors(left_motor_controller, right_motor_controller)
  battery = get_battery([left_motor_controller, right_motor_controller])
  gps = get_gps()
  return Robot(id, motors, battery, gps)

def get_left_motor_controller():
  motor_config = get_left_motor_config()
  port_name = motor_config["port_name"]
  return ConsoleMotorController(port_name)

def get_right_motor_controller():
  motor_config = get_right_motor_config()
  port_name = motor_config["port_name"]
  return ConsoleMotorController(port_name)

def get_motors(left_motor_controller, right_motor_controller):
  return {
    "left": Motor(left_motor_controller),
    "right": Motor(right_motor_controller)
  }

def get_battery(motor_controllers):
  voltage_sensor = PololuG2VoltageSensor(motor_controllers)
  return Battery(voltage_sensor)

def get_gps():
  gps_module = SixfabGPSModule()
  return GPS(gps_module)

start_robot()
