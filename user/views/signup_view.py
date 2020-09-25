from user.models.profile_model import *
from user.models.user_model import *
from user.models.entity_model import *
from user.serializers.profile_serializer import *
from user.serializers.user_serializer import *
from user.serializers.entity_serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

class SignUpView(APIView):

    def get(self, request, format=None):
        user = Users.objects.all()
        profile = Profile.objects.all()
        entity=Entity.objects.all()
        user_serializer = UsersSerializer(user,many=True)
        profile_serializer = ProfileSerializer(profile, many=True)
        entity_serializer = EntitySerializer(entity, many=True)
        return Response(
            {
                'entity':entity_serializer.data,
                'user':user_serializer.data,
                'profile': profile_serializer.data
            })

    def post(self, request, format=None):
        user={
            "first_name": request.data['first_name'],
            "last_name": request.data['last_name'],
            "email": request.data['email'],
            "username": request.data['username'],
            "password": make_password(request.data['password']),
            "created_at": request.data['created_at'],
            "updated_at":request.data['updated_at'],
            "created_by": request.data['created_by'],
            "updated_by":request.data['updated_by']
        }
        entity={
            "company_name": request.data['company_name'],
            "first_name": request.data['first_name'],
            "last_name": request.data['last_name'],
            "created_at": request.data['created_at'],
            "updated_at":request.data['updated_at'],
            "created_by": request.data['created_by'],
            "updated_by":request.data['updated_by']
        }

        user_serializer = UsersSerializer(data=user)
        entity_serializer = EntitySerializer(data=entity)

        if user_serializer.is_valid() and entity_serializer.is_valid():
            entity_serializer.save()
            user_serializer.save()
            users=Users.objects.last()
            entities=Entity.objects.last()
            id_user=users.id
            id_entity= entities.id
            key= make_password(user_serializer.data['username'])
            secret= user_serializer.data['password']
            profiles={
                'photo':None,
                'entity': id_entity,
                'users':id_user,
                'secret': secret,
                'key':key,
                'is_first_user':True
            }
            
            profile_serializer= ProfileSerializer(data= profiles)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({'entity':entity_serializer.data,'user':user_serializer.data,'profile':profile_serializer.data}, status = status.HTTP_201_CREATED)
            else:
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)