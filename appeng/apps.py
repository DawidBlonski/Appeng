from django.apps import AppConfig

class EngappConfig(AppConfig):
    name = 'appeng'

    def ready(self):
        import appeng.signals


