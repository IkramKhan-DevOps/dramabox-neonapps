from django.forms import ModelForm
from src.services.users.models import User


class UserProfileForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name',
        ]

