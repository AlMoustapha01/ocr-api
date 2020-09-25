from django.db import models
from user.models.profile_model import *
from .application_model import *

class ProfileByApplication(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    profile = models.ForeignKey(Profile, models.DO_NOTHING, db_column='profile', blank=True, null=True)
    application = models.ForeignKey(Application, models.DO_NOTHING, db_column='application', blank=True, null=True)
    can_send_sms = models.BooleanField(blank=True, null=True)
    can_send_email = models.BooleanField(blank=True, null=True)
    can_send_web_push = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = 'True'
        db_table = 'ProfileByApplication'