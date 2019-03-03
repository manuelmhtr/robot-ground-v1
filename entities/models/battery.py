import threading
from entities.models.component import Component

class Battery(Component):
  MIN_VOLTAGE_PER_CELL = 3.3
  MAX_VOLTAGE_PER_CELL = 4.2
  READ_VOLTAGE_INTERVAL = 1
  ITEMS_FOR_AVERAGE = 10

  def __init__(self, cells, voltage_sensor):
    super().__init__()
    self.cells = cells
    self.voltage = None
    self.power_percentage = None
    self.voltage_sensor = voltage_sensor
    self.voltage_values = []
    self.start_reading_volatge()

  def calculate_power_percentage(self, voltage):
    min_voltage = self.cells * self.MIN_VOLTAGE_PER_CELL
    max_voltage = self.cells * self.MAX_VOLTAGE_PER_CELL
    diff = max_voltage - min_voltage
    value = 100.0 * (voltage - min_voltage) / diff
    return max(0.0, min(100.0, value))

  def set_voltage(self, voltage):
    if (self.voltage != voltage):
      self.voltage = voltage
      self.power_percentage = self.calculate_power_percentage(self.voltage)
      super().report_change()

  def start_reading_volatge(self):
    self.read_voltage()
    threading.Timer(self.READ_VOLTAGE_INTERVAL, self.start_reading_volatge).start()

  def read_voltage(self):
    voltage = round(self.voltage_sensor.get_voltage(), 2)
    self.voltage_values.append(voltage)
    if len(self.voltage_values) > self.ITEMS_FOR_AVERAGE:
      self.voltage_values.pop(0)
    avg_voltage = sum(self.voltage_values) / len(self.voltage_values)
    self.set_voltage(avg_voltage)

  def get_status(self):
    return {
      "voltage": self.voltage,
      "percentage": self.power_percentage
    }
