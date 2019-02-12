import pubnub
from infrastructure.config import get_pubnub_config, get_robot_id;
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

class CommandListener(SubscribeListener):
    def message( self, pubnub, event ):
        print( "Command: ", event.message, event.user_metadata, event.channel, event.timetoken )

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
