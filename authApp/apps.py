from django.apps import AppConfig


class AuthappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authApp'

    def ready(self):
        import authApp.models.signals
        from jobs import updater

        updater.start()
        
