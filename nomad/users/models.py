from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class User(AbstractUser):
    class LanguageChoice(models.TextChoices):
        KR = ("kr","Korean")
        EN = ("en","English")

    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default="")
    is_host = models.BooleanField(default=False)
    language =models.CharField(max_length=2, choices=LanguageChoice.choices)


# class UserManger(BaseUserManager):
#     def creat_user(
#         self,
#         username:str,
#         email:str,
#         first_name:str,
#         last_name:str,
#         password:str,
#     )->User:
#         if not username:
#             raise ValueError("username은 필수다 ")
        
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#             last_name=last_name,
#             first_name=first_name
#             )
#         user.set_password(password)
#         user.save()
#         return user
