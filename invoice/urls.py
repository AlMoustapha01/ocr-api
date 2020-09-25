from django.urls import path,include
from invoice.views.invoice_view import *
from invoice.views.invoicerow_view import *
from invoice.views.file_view import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   #### invoices views
    path('invoices/',InvoiceView.as_view(),name='applications'),
    path('invoices/<int:id>/',InvoiceViewById.as_view(),name='application_by_id'),

   #### invoicerows views
    path('invoicerows/',InvoiceRowView.as_view(),name="invoices"),
    path('invoicerows/<str:id>/',InvoiceRowViewById.as_view(),name="invoice_by_id"),

    #### files views
    path('files/',FileView.as_view(),name="files"),
    path('files/<str:id>/',FileViewById.as_view(),name="file_by_id"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)