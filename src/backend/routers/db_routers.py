from operator import mod


class AuthRouter:
    # route_app_labels = {'auth', 'contenttypes'} #aplikacje
    # route_app_labels = {auth', 'contenttypes', 'sessions', 'admin'} żeby admin miał dostęp do bazy
    # route_app_labels = {'auth', 'contenttypes', 'sessions', 'admin', 'users', 'appuser' 'censys_api_id', 'censys_secret', 'shodan_username', 'shodan_api_key' } #aplikacje
    route_app_labels = {
        "auth",
        "contenttypes",
        "sessions",
        "admin",
        "users",
    }  # aplikacje

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "users_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "users_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "users_db"
        return None

        Vulnerabilities


class VulnerabilitiesRouter:
    route_app_labels = {"vulnerabilities"}  # aplikacje

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "vulns_db"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "vulns_db"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "vulns_db"
        return None
