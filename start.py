import pubnub
from infrastructure.config import get_pubnub_config, get_robot_id, get_usb_port_name, get_right_motor_config
from infrastructure.motor_controllers.pololu_g2 import PololuG2MotorController
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

# Motor config
rmotor_config = get_right_motor_config();
right_motor = PololuG2MotorController(get_usb_port_name(), rmotor_config["device_number"])

class CommandListener(SubscribeListener):
  def message( self, pubnub, event ):
    print( "Command: ", event.message )
    command = event.message['command']
    data = event.message["data"]
    if (command == "SET_SPEED"):
      speed = int(data["speed"])
      if (data["motor"] == "right"):
        right_motor.set_speed(speed)

# Pubnub config
config = get_pubnub_config()
channel = get_robot_id()
pnconfig = PNConfiguration()
pnconfig.subscribe_key = config["subscribe_key"]
pnconfig.publish_key = config["publish_key"]
pnconfig.secret_key = config["secret_key"]
pnconfig.ssl = config["ssl"]
pubnub = PubNub(pnconfig)

pubnub.add_listener(CommandListener())
pubnub.subscribe().channels(channel).execute()
