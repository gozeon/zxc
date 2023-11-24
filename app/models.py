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

    def my_menu(self):
        return self.menu_set.filter(delete_date__isnull=True)


class Menu(models.Model):
    name = models.CharField(max_length=10)
    app = models.ForeignKey(Application, on_delete=models.CASCADE)

    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=10, unique=True)
    content = models.TextField()

    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=10)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.PROTECT)

    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField(verbose_name="date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name
