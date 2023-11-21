from django.urls import path
from . import views

app_name = "dash"
urlpatterns = [
    path("", views.index, name="index"),
    path("app/", views.app, name="app"),
    path("del/app/<int:app_id>", views.del_app, name="del_app"),
    path("pub/app/<int:app_id>", views.pub_app, name="pub_app"),
]
