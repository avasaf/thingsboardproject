#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.base import BaseCommand
from mqtt_read_client import receive_data
from mqtt_write_client import send_data
from pymodbus.client import ModbusTcpClient


class read_modbus_data(BaseCommand):
    help = 'Read modbus data'

    def add_arguments(self, parser):
        parser.add_argument('ip', type=str, help='IP address of the modbus device')

    def handle(self, *args, **options):
        ip = options['ip']
        client = ModbusTcpClient(ip)
        client.connect()
        result = client.read_holding_registers(0, 10)
        print(result.registers)
        client.close()


class write_modbus_data(BaseCommand):
    help = 'Write modbus data'

    def add_arguments(self, parser):
        parser.add_argument('ip', type=str, help='IP address of the modbus device')

    def handle(self, *args, **options):
        ip = options['ip']
        client = ModbusTcpClient(ip)
        client.connect()
        client.write_register(0, 42)
        client.close()


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    send_data("{\"temperature\": 23}")
    receive_data()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()