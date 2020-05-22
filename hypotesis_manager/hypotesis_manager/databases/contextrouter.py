class ContextRouter:
    """
    A router to control all database operations on models in the context applications.
    """
    route_app_labels = {'context'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read context models go to hypotesis_context.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'hypotesis_context'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write context models go to hypotesis_context.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'hypotesis_context'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the context apps is involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the context apps only appear in the 'hypotesis_context' database.
        """
        if app_label in self.route_app_labels:
            return db == 'hypotesis_context'
        return db == 'default'
