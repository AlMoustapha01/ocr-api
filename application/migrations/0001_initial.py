# Generated by Django 3.0.5 on 2020-09-21 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(blank=True, max_length=255, null=True)),
                ('app_code', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('entity', models.ForeignKey(blank=True, db_column='entity', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Entity')),
            ],
            options={
                'db_table': 'application',
                'managed': 'True',
            },
        ),
        migrations.CreateModel(
            name='ProfileByApplication',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('can_send_sms', models.BooleanField(blank=True, null=True)),
                ('can_send_email', models.BooleanField(blank=True, null=True)),
                ('can_send_web_push', models.BooleanField(blank=True, null=True)),
                ('application', models.ForeignKey(blank=True, db_column='application', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.Application')),
                ('profile', models.ForeignKey(blank=True, db_column='profile', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Profile')),
            ],
            options={
                'db_table': 'ProfileByApplication',
                'managed': 'True',
            },
        ),
    ]
