class Component(object):
  def __init__(self):
    self.on_change_callback = None

  def on_change(self, callback):
    self.on_change_callback = callback
  
  def report_change(self):
    if self.on_change_callback:
      self.on_change_callback(self.get_status())
  
  def get_status(self):
    return {}
