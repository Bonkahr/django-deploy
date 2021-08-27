from django import forms
from loginApp.models import NewUser


class NewUsers(forms.ModelForm):

    class Meta:
        model = NewUser
        fields = '__all__'

