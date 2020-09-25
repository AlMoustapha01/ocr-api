from django.contrib import admin
from invoice.models.invoice_model import *
from invoice.models.invoicerow_model import *
from invoice.models.file_model import *
# Register your models here.
admin.site.register(Invoice)
admin.site.register(Invoicerow)
admin.site.register(File)