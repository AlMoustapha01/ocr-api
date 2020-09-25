from rest_framework import serializers
from invoice.models.invoice_model import *

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

