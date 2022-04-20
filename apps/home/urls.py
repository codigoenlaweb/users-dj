from django.urls import path

# views
from .views import *

app_name='myapp'
urlpatterns = [
    path('', My_app.as_view(), name='myapp'),
]
