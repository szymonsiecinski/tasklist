from django.contrib.auth.models import User


class AuthenticationBackend(object):

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user is not None:
                if user.check_password(password):
                    return user
            else:
                return None
        except User.DoesNotExist:
            return None
