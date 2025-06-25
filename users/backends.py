from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class EmailRollNumberBackend(BaseBackend):
    def authenticate(self, request, email=None, roll_number=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=email, roll_number=roll_number)
            if user.check_password(password): 
                return user
        except CustomUser.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None 