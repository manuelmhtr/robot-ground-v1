class Battery(object):
  MIN_VOLTAGE_PER_CELL = 3.3
  MAX_VOLTAGE_PER_CELL = 4.2

  def __init__(self, cells, voltage_sensor):
    self.cells = cells
    self.voltage_sensor = voltage_sensor

  def calculate_percentage(self, voltage):
    min_voltage = self.cells * self.MIN_VOLTAGE_PER_CELL
    max_voltage = self.cells * self.MAX_VOLTAGE_PER_CELL
    diff = max_voltage - min_voltage
    value = 100.0 * (voltage - min_voltage) / diff
    return max(0.0, min(100.0, value))
  
  def get_status(self):
    voltage = self.voltage_sensor.get_voltage()
    percentage = self.calculate_percentage(voltage)
    return {
      "voltage": voltage,
      "percentage": percentage
    }
