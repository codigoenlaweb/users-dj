# django
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
# myapp
from django.conf import settings
from .forms import RegisterUserForm


# Views
class Home_view(TemplateView):
    template_name = "user/home_view.html"


class RegisterView(FormView):
    form_class = RegisterUserForm
    template_name = "user/register.html"
    success_url = reverse_lazy("myapp:myapp")

    def form_valid(self, form):
        user = form.save()
        
        send_mail(
            'Registration completed',
            f'{user.first_name} you have successfully registered',
            settings.EMAIL_HOST_USER,
            [user.email]
        )
        
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

class LoginView_form(LoginView):
    template_name = 'user/login_view.html'


class LogoutView_form(LogoutView):
    pass


class ChangePassword_form(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/changepassword_view.html'
    success_url = reverse_lazy('home:login')