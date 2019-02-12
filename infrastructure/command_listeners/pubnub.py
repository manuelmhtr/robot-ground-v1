from infrastructure.sockets.pubnub import PubnubSocket

class PubnubCommandListener(object):
  def __init__(self, channel):
    self.events = {}
    self.socket = PubnubSocket(channel, self.handle_message)

  def on(self, event_name, callback):
    self.events[event_name] = callback
  
  def handle_message(self, message):
    command = message["command"]
    data = message["data"]
    if (self.events[command]):
      self.events[command](data)
