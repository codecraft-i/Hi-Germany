from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MessageUser

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class MessageUserForm(forms.ModelForm):
    class Meta:
        model = MessageUser
        fields = ['name', 'body']