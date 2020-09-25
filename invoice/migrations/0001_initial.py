# Generated by Django 3.0.5 on 2020-09-22 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0002_auto_20200922_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_id', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice_date', models.CharField(blank=True, max_length=255, null=True)),
                ('prize', models.CharField(blank=True, max_length=255, null=True)),
                ('vat', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'invoice',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Invoicerow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('prize', models.CharField(blank=True, max_length=255, null=True)),
                ('journal_type', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('invoice', models.ForeignKey(blank=True, db_column='invoice', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoice.Invoice')),
            ],
            options={
                'db_table': 'invoicerow',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('application', models.ForeignKey(blank=True, db_column='application', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.Application')),
                ('invoice', models.ForeignKey(blank=True, db_column='invoice', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoice.Invoice')),
            ],
        ),
    ]
