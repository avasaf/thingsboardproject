#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from mqtt_read_client import receive_data
from mqtt_write_client import send_data


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
