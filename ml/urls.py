from django.urls import path
from . import   views
urlpatterns = [
   path('', views.forminfo, name='forminfo'),
    
]
