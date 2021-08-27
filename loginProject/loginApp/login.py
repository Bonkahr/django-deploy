from django import forms
from loginApp.models import Login


class UserLogin(forms.ModelForm):

    class Meta:
        model = Login
        fields = '__all__'
