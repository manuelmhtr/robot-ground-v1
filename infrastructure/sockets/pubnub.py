import pubnub
from infrastructure.config import get_pubnub_config
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

class PubnubSocket(object):
  def __init__(self):
    config = get_pubnub_config()
    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = config["subscribe_key"]
    pnconfig.publish_key = config["publish_key"]
    pnconfig.secret_key = config["secret_key"]
    pnconfig.ssl = config["ssl"]

    self.pubnub = PubNub(pnconfig)
  
  def add_listener(self, listener):
    self.pubnub.add_listener(listener)

  def subscribe(self, channel):
    self.pubnub.subscribe().channels(channel).execute()

  def publish(self, channel, data):
    self.pubnub.publish().channel(channel).message(data).sync()

pubnub_socket = PubnubSocket()
