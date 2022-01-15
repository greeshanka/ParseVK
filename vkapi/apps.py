from django.apps import AppConfig


class VkapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vkapi'

    def ready(self):
        from .views import sch
        sch()
