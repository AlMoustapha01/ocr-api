from user.models.profile_model import *
from user.models.user_model import *
from user.serializers.profile_serializer import *
from user.serializers.user_serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

class CollaboratorView(APIView):

    def get(self, request, format=None):
        user = Users.objects.all()
        profile = Profile.objects.all()
        user_serializer = UsersSerializer(user,many=True)
        profile_serializer = ProfileSerializer(profile, many=True)
        return Response(
            {'user':user_serializer.data,
            'profile': profile_serializer.data
            })

    def post(self, request, format=None):
        print(request.data)
        request.data['user']['password']=make_password(request.data['user']['password'])
        user_serializer = UsersSerializer(data=request.data['user'])
        profile= request.data['profile']
        if user_serializer.is_valid() :
            user_serializer.save()
            users=Users.objects.filter(username=request.data['user']['username'])
            print(users)
            user= users[0]
            print(user)
            id_user=user.id
            key= make_password(user_serializer.data['username'])
            secret= user_serializer.data['password']
            profile['users'] = id_user
            profile['key'] =key
            profile['secret'] = secret
            profile_serializer= ProfileSerializer(data= profile)
            if profile_serializer.is_valid():
                profile_serializer.save()
                return Response({'user':user_serializer.data,'profile':profile_serializer.data}, status = status.HTTP_201_CREATED)
            else:
                return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)