from django.urls import path

# views
from .views import *

app_name='home'

urlpatterns = [
    path('', Home_view.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView_form.as_view(), name="login"),
    path('logout/', LogoutView_form.as_view(), name="logout"),
    path('changepassword/', ChangePassword_form.as_view(), name="changepassword"),
]
