class AuthRouter:
    """
    python manage.py migrate users --database=users
    """

    # users - nazwa bazy dancyh
    route_app_labels = {
        "users",
        "admin",
        "contenttypes",
        "sessions",
        # "auth",
    }
    # po dodaniu "admin", "contenttypes", "sessions"
    # python manage.py migrate --database=users

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "users"

        return None
