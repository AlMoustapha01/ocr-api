from django.db import models 
from invoice.models.invoice_model import Invoice

class Invoicerow(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    prize = models.CharField(max_length=255, blank=True, null=True)
    journal_type = models.CharField(max_length=255, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='invoice', blank=True, null=True)    
    created_at = models.DateField(blank=True, null=True)
    updated_at = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    updated_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'invoicerow'