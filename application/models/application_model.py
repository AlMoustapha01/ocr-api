from django.db import models
from user.models.entity_model import *

class Application(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    app_name = models.CharField(max_length=255, blank=True, null=True)
    app_code = models.CharField(max_length=255, blank=True, null=True)
    entity = models.ForeignKey(Entity, models.DO_NOTHING, db_column='entity', blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = 'True'
        db_table = 'application'