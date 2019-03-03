from pubnub.pubnub import SubscribeListener
from infrastructure.sockets.pubnub import pubnub_socket

class CommandListener(SubscribeListener):
  def __init__(self, on_message):
    self.on_message = on_message
    super().__init__()

  def message(self, pubnub, event):
    self.on_message(event.message)

class PubnubCommandListener(object):
  def __init__(self, channel):
    self.events = {}
    self.socket = pubnub_socket
    self.socket.subscribe(channel)

    listener = CommandListener(self.handle_message)
    self.socket.add_listener(listener)

  def on(self, event_name, callback):
    self.events[event_name] = callback
  
  def handle_message(self, message):
    command = message["command"]
    data = message["data"]
    if (self.events[command]):
      self.events[command](data)
