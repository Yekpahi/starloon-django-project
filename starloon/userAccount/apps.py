from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userAccount'
  # add this
    def ready(self):
        import userAccount.signals  # noqa