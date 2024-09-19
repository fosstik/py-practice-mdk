from django.apps import AppConfig


class Practic13Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'practic13'

    def ready(self) -> None:
        import practic13.signals
