from django.http import JsonResponse
from modbus_client import write_registers

def write_modbus_data(request):
    # Get the incoming data from Thingsboard
    data = request.POST.get('data')
    # Write the data to the Modbus server
    write_registers("localhost", 502, 0, data)
    return JsonResponse({"status": "success"})
