from django.apps import AppConfig


class OfficersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users.officers'

    def ready(self):
        import users.officers.signals