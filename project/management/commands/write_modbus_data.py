from django.core.management.base import BaseCommand
from pymodbus.client import ModbusTcpClient

class Command(BaseCommand):
    help = 'Write modbus data'

    def handle(self, *args, **options):
        client = ModbusTcpClient("localhost", 502)
        client.connect()
        client.write_registers(0, [1])
        client.close()
        print("Data written to modbus server")
