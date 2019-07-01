from django import forms
from .models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('ap', 'hp', 'mp', 'event')