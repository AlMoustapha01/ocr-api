from django.db import models

class Profile(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    entity = models.ForeignKey('Entity', models.DO_NOTHING, db_column='entity', blank=True, null=True)
    users = models.ForeignKey('Users', models.DO_NOTHING, db_column='users', blank=True, null=True)
    photo = models.ImageField(max_length=255, blank=True, null=True)
    is_first_user = models.BooleanField(blank=True, null=True)
    key = models.CharField(max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = 'True'
        db_table = 'profile'