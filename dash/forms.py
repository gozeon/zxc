from django import forms
from app.models import Application


class AppForm(forms.ModelForm):
    class Meta:
        model = Application

        fields = [
            "name",
            "desc",
        ]

        widgets = {
            "desc": forms.Textarea
        }

