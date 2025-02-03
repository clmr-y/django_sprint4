from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Used in settings file."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = "Блог"
