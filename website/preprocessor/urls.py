from django.urls import path
from .views import *

urlpatterns = [
    path('', file_uploader_view, name='uploader'),
]
