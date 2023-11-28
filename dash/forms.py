from django import forms
from app.models import Application, Menu, MenuItem, Page


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


class MenuForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["app"].queryset = Application.objects.filter(create_user__isnull=False)
        self.fields['app'].label_from_instance = lambda obj: "%s(%s)" % (obj.name, obj.pk)

    class Meta:
        model = Menu

        fields = [
            "name",
            "app",
        ]


class MenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["page"].queryset = Page.objects.filter(create_user__isnull=False)

    class Meta:
        model = MenuItem
        fields = [
            "name",
            "page",
        ]


class PageForm(forms.ModelForm):
    class Meta:
        model = Page

        fields = [
            "name",
            "content",
        ]
