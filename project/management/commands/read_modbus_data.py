from django.core.management.base import BaseCommand
from pymodbus.client import ModbusTcpClient

class Command(BaseCommand):
    help = 'Read modbus data'

    def handle(self, *args, **options):
        client = ModbusTcpClient("localhost", 502)
        client.connect()
        result = client.read_holding_registers(0, 1)
        client.close()
        print(result.registers)
