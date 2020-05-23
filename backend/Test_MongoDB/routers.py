class Test_MongoDBRouter(object):
    """
    A router to control all database operations on models in
    the Test_MongoDB application
    """
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on Test_MongoDB models to 'MongoDB'
        """
        if model._meta.app_label == 'Test_MongoDB':
            return 'MongoDB'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'Test_MongoDB':
            return 'MongoDB'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'Test_MongoDB' app only appears on the 'other' db
        """
        if db == 'MongoDB':
            return model._meta.app_label == 'Test_MongoDB'
        elif model._meta.app_label == 'Test_MongoDB':
            return False
        return None