from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomrUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", 'username']
    # def __init__(self, *args: Any, **kwargs: Any) -> None:
    #     super().__init__(*args, **kwargs)

