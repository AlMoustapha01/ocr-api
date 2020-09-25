from django.db import models 

class Invoice(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    client_name = models.CharField(max_length=255, blank=True, null=True)
    invoice_id = models.CharField(max_length=255, blank=True, null=True)
    invoice_date = models.CharField(max_length=255, blank=True, null=True)
    prize = models.CharField(max_length=255, blank=True, null=True)
    vat = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'invoice'


