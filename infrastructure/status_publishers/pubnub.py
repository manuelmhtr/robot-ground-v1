from infrastructure.sockets.pubnub import pubnub_socket

class PubnubStatusPublisher(object):
  def __init__(self, channel):
    self.channel = channel
    self.socket = pubnub_socket

  def publish(self, data):
    self.socket.publish(self.channel, data)
