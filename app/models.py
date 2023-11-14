from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=100, blank=True)
    pub_date = models.DateTimeField(verbose_name="date published", null=True, blank=True, default=None)

    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=10)
    app = models.ForeignKey(Application, on_delete=models.CASCADE)

    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=10)
    link = models.CharField(max_length=50)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name
