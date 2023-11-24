from django import forms
from app.models import Application, Page


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


class PageForm(forms.ModelForm):
    class Meta:
        model = Page

        fields = [
            "name",
            "content",
        ]
