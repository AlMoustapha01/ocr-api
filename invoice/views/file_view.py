from django.shortcuts import render
from invoice.models.file_model import *
from invoice.serializers.file_serializer import *
from rest_framework.response import Response
from rest_framework import mixins,views
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.parsers import FileUploadParser
from pyocr_test import extraction,features,invoiceTreatment,utils
# Create your views here.


class FileView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    parser_class = (FileUploadParser,)
    serializer_class = FileSerializer
    queryset = File.objects.all()
    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)



class FileViewById(views.APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, id):
        try:
            return File.objects.get(pk=id)
        except File.DoesNotExist:
            raise status.HTTP_400_BAD_REQUEST

    def get(self, request, id, format=None):
        file = self.get_object(id)
        serializer =FileSerializer(file)
        file=serializer.data['file']
        ts= invoiceTreatment.pyocr('.'+file)
        res={'File':serializer.data,'ocr':ts}
        return Response(res,status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        file = self.get_object(id)
        serializer = FileSerializer(file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        file = self.get_object(id)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)