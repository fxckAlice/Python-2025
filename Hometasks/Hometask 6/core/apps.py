from django.apps import AppConfig
import os

class CoreConfig(AppConfig):
    name = "core"

    def ready(self):
        if os.environ.get("RUN_MAIN") != "true":
            return
        from core.repository.sqlite_init import init_sqlite
        init_sqlite()
