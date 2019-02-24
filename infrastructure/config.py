from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_pubnub_config():
  return {
    "publish_key": getenv("PUBNUB_PUBLISH_KEY"),
    "subscribe_key": getenv("PUBNUB_SUBSCRIBE_KEY"),
    "secret_key": getenv("PUBNUB_SECRET_KEY"),
    "ssl": True
  }

def get_robot_id():
  return getenv("ROBOT_ID")

def get_right_motor_config():
  return {
    "port_name": int(getenv("RIGHT_MOTOR_PORT_NAME")),
    "device_number": int(getenv("RIGHT_MOTOR_DEVICE_NUMBER"))
  }

def get_left_motor_config():
  return {
    "port_name": int(getenv("LEFT_MOTOR_PORT_NAME")),
    "device_number": int(getenv("LEFT_MOTOR_DEVICE_NUMBER"))
  }
