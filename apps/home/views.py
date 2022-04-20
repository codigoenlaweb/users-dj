from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.users.models import User

# myapp
from apps.users.mixing import UserLogedMixing

# Create your views here.

class My_app(LoginRequiredMixin, UserLogedMixing,TemplateView):
    template_name = "home/my_app.html"


