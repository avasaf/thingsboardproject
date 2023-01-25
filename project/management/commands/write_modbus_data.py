from django.core.management.base import BaseCommand
from modbus_client import read_holding_registers
from mqtt_write_client import send_data

class Command(BaseCommand):
    help = 'Read data from Modbus Simulator and send it to Thingsboard.io'

    def handle(self, *args, **options):
        # Read data from Modbus Simulator
        data = read_holding_registers("localhost", 502, 0, 10)
        # Send data to Thingsboard.io
        send_data(data)
