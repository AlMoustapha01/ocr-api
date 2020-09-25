from django.db import models 
from application.models.application_model import Application
from invoice.models.invoice_model import Invoice

class File(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    file = models.FileField(blank=False, null=False)
    application = models.ForeignKey(Application, models.DO_NOTHING, db_column='application', blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='invoice', blank=True, null=True) 
    def __str__(self):
        return self.file.name