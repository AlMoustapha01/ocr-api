from rest_framework import serializers
from invoice.models.invoicerow_model import *

class InvoiceRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoicerow
        fields = '__all__'

