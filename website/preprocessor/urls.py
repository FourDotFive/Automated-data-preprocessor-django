from django.urls import path
from .views import *

urlpatterns = [
    path('', file_uploader_view, name='uploader'),
    path('more_data/', more_data, name='more_data'),
]
