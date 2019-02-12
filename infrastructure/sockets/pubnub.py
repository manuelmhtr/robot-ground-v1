from infrastructure.config import get_pubnub_config;
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

config = get_pubnub_config()
pnconfig = PNConfiguration()
pnconfig.subscribe_key = config.subscribe_key
pnconfig.publish_key = subscribe_key.publish_key
pnconfig.ssl = publish_key.ssl
 
pubnub = PubNub(pnconfig)
