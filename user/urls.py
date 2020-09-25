from django.urls import path,include
from user.views.entity_view import *
from user.views.user_view import *
from user.views.profile_view import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
import djoser
from user.views.collaborator_view import *
from user.views.signup_view import *
schema_view = get_schema_view(
   openapi.Info(
      title="OCR API",
      default_version='v1',
      description="OCR Api description ...",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
   #### entity views
    path('entities/',EntityView.as_view(),name='entities'),
    path('entities/<str:id>/',EntityViewById.as_view(),name='entity_by_id'),
   #### users views
    path('users/',UsersView.as_view(),name='users'),
    path('users/<int:id>/',UsersViewById.as_view(),name='user_by_id'),
    #authentifation
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
   #### profils views
    path('profiles/',ProfileView.as_view(),name='profiles'),
    path('profiles/<str:id>',ProfileViewById.as_view(),name='profile_by_id'),
   #### collaborateur
    path('collaborators/', CollaboratorView.as_view(),name='collaborators'),
   #### signup
    path('signup/',SignUpView.as_view(),name='signup'),
   #### documentation
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
