from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    name = models.CharField(max_length=20)
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(verbose_name="date published", null=True, blank=True, default=None)
    create_date = models.DateTimeField(verbose_name="date created", auto_now_add=True)
    delete_date = models.DateTimeField("date deleted", default=None, null=True, blank=True)

    def __str__(self):
        return self.name
