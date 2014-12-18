#coding: utf-8

from sqlalchemy import types, ForeignKey
try:
    from django.apps import apps as django_apps
except ImportError:
    from django.db.models.loading import AppCache, get_model

    django_apps = AppCache()


def simple(typ):
    return lambda field: typ()


def varchar(field):
    return types.String(length=field.max_length)


def foreign_key(field):
    target = field.rel.to
    if type(target) == str:
        app_label, model_name = target.split('.')
        target = django_apps.get_model(app_label, model_name)
        if not target:
            print "Warning aldjemy: can't find model {}.{}".format(app_label, model_name)
            return types.Integer()
    target = target._meta
    target_table = target.db_table
    target_pk = target.pk.column
    return types.Integer, ForeignKey('%s.%s' % (target_table, target_pk))
