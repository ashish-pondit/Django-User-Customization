from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User
from custom_user.models import MyUser
from django.contrib.auth import get_user_model


class EmailAndUsernameBackend(BaseBackend):
    # def authenticate(self, request, username=None, email=None, password=None):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}

        try:
            user = get_user_model().objects.get(**kwargs)
            if user.check_password(password):
                return user
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None

