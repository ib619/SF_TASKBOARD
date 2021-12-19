from django.apps import AppConfig


class TbConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TB'

    def ready(self):
        import TB.signals



