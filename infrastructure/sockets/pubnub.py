import pubnub
from infrastructure.config import get_pubnub_config
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub, SubscribeListener

class CommandListener(SubscribeListener):
  def __init__(self, on_message):
    self.on_message = on_message
    super().__init__()

  def message(self, pubnub, event):
    self.on_message(event.message)

class PubnubSocket(object):
  def __init__(self, channel, on_message):
    config = get_pubnub_config()
    pnconfig = PNConfiguration()
    pnconfig.subscribe_key = config["subscribe_key"]
    pnconfig.publish_key = config["publish_key"]
    pnconfig.secret_key = config["secret_key"]
    pnconfig.ssl = config["ssl"]

    self.on_message = on_message
    self.listener = CommandListener(self.on_message)
    self.pubnub = PubNub(pnconfig)
    self.pubnub.add_listener(self.listener)
    self.pubnub.subscribe().channels(channel).execute()
