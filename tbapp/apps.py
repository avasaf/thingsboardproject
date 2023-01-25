from django.apps import AppConfig

class ProjectConfig(AppConfig):
    name = 'project'

    def ready(self):
        import project.management.commands.read_modbus_data
        import project.management.commands.write_modbus_data
