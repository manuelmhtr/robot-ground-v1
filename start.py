from infrastructure.config import is_live_env, get_robot_id, get_right_motor_config, get_left_motor_config
from infrastructure.command_listeners.pubnub import PubnubCommandListener
from infrastructure.gps_modules.sixfab_base import SixfabBaseGPSModule
from infrastructure.gps_modules.mock import MockGPSModule
from infrastructure.motor_controllers.pololu_g2 import PololuG2MotorController
from infrastructure.motor_controllers.console import ConsoleMotorController
from infrastructure.status_publishers.console import ConsoleStatusPublisher
from infrastructure.status_publishers.pubnub import PubnubStatusPublisher
from infrastructure.voltage_sensors.pololu_g2 import PololuG2VoltageSensor
from infrastructure.voltage_sensors.mock import MockVoltageSensor
from controllers.robot import RobotController
from entities.models.battery import Battery
from entities.models.motor import Motor
from entities.models.robot import Robot
from entities.models.gps import GPS

def start_robot():
  robot = get_robot()
  command_listener = get_command_listener(robot.id)
  status_publisher = get_status_publisher(robot.id)
  controller = RobotController(robot, command_listener, status_publisher)
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
  if is_live_env():
    motor_config = get_left_motor_config()
    port_name = motor_config["port_name"]
    return PololuG2MotorController(port_name)
  else: 
    return ConsoleMotorController()

def get_right_motor_controller():
  if is_live_env():
    motor_config = get_right_motor_config()
    port_name = motor_config["port_name"]
    return PololuG2MotorController(port_name)
  else: 
    return ConsoleMotorController()

def get_motors(left_motor_controller, right_motor_controller):
  return {
    "left": Motor(left_motor_controller),
    "right": Motor(right_motor_controller)
  }

def get_battery(motor_controllers):
  if is_live_env():
    voltage_sensor = PololuG2VoltageSensor(motor_controllers)
  else: 
    voltage_sensor = MockVoltageSensor()
  return Battery(2, voltage_sensor)

def get_gps():
  if is_live_env():
    gps_module = SixfabBaseGPSModule()
  else: 
    gps_module = MockGPSModule()
  return GPS(gps_module)

def get_command_listener(robot_id):
  channel = robot_id + ':commands'
  return PubnubCommandListener(channel)

def get_status_publisher(robot_id):
  channel = robot_id + ':status'
  if is_live_env():
    return PubnubStatusPublisher(channel)
  else: 
    return ConsoleStatusPublisher()

start_robot()
