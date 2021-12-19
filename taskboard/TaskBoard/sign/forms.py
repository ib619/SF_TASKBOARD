from django import forms
from .models import Member
from django.forms import ModelForm


class MemberForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Member
        fields = ('__all__')
