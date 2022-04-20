from django.db import models
from django.contrib.auth.models import UserManager

class UserManagers(UserManager, models.Manager):

    def get_user_id(self, user_id):
        return self.get(id=user_id)