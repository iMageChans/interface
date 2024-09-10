# my_project/routers/db_router.py

class DBRouter:
    def db_for_read(self, model, **hints):
        """指向读取数据库"""
        return 'replica'

    def db_for_write(self, model, **hints):
        """指向写入数据库"""
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """允许在两个数据库之间的关系"""
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """只允许迁移到写数据库"""
        return db == 'default'
