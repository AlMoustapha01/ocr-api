from django.urls import path,include
from application.views.application_view import ApplicationView,ApplicationViewById
from application.views.profilebyapplication_view import ProfileByApplicationView,ProfileByApplicationViewById
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
   #### applications views
    path('applications/',ApplicationView.as_view(),name='applications'),
    path('applications/<int:id>/',ApplicationViewById.as_view(),name='application_by_id'),

   #### profilebyapplications views
    path('profilebyapplications/',ProfileByApplicationView.as_view(),name="profilebyapplications"),
    path('profilebyapplications/<str:id>/',ProfileByApplicationViewById.as_view(),name="profilebyapplication_by_id"),

]
