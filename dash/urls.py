from django.urls import path
from . import views

app_name = "dash"
urlpatterns = [
    path("", views.index, name="index"),

    path("app/", views.app, name="app"),
    path("del/app/<int:app_id>", views.del_app, name="del_app"),
    path("pub/app/<int:app_id>", views.pub_app, name="pub_app"),
    path("new/app/", views.new_app, name="new_app"),
    path("detail/app/<int:app_id>", views.detail_app, name="detail_app"),

    path("menu/", views.menu, name="menu"),
    path("del/menu/<int:menu_id>", views.del_menu, name="del_menu"),

    path("page/", views.page, name="page"),
    path("del/page/<int:page_id>", views.del_page, name="del_page"),
]
