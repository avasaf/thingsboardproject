from pymodbus.client import ModbusTcpClient as ModbusClient

def read_holding_registers(ip_address, port, address, count):
    client = ModbusClient(ip_address, port)
    client.connect()
    result = client.read_holding_registers(address, count)
    client.close()
    return result.registers

def write_registers(ip_address, port, address, values):
    client = ModbusClient(ip_address, port)
    client.connect()
    client.write_registers(address, values)
    client.close()
