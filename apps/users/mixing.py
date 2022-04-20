from apps.users.models import User


class UserLogedMixing(object):
    
    def get_context_data(self, **kwargs):
        context = super(UserLogedMixing, self).get_context_data(**kwargs)
        context['user_active'] = User.objects.get_user_id(self.request.user.id)
        return context