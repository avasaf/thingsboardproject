from django.db import models
from pymodbus.client import ModbusTcpClient

class ModbusDevice(models.Model):
    ip_address = models.GenericIPAddressField()
    port = models.PositiveSmallIntegerField()

    def read_registers(self, address, count):
        with ModbusTcpClient(self.ip_address, self.port) as client:
            result = client.read_holding_registers(address, count)
        return result.registers

class Boiler(ModbusDevice):
    temperature = models.FloatField()
    pressure = models.FloatField()
    gas = models.FloatField()
    on_off = models.BooleanField()

    def update_data(self):
        self.temperature = self.read_registers(1, 1)
        self.pressure = self.read_registers(2, 1)
        self.gas = self.read_registers(3, 1)
        self.on_off = self.read_registers(4, 1)
        self.save()
