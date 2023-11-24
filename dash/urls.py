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
    path("new/menu/", views.new_menu, name="new_menu"),
    path("detail/menu/<int:menu_id>", views.detail_menu, name="detail_menu"),

    path("<int:menu_id>/menuitem/", views.menuItem, name="menuItem"),
    path("<int:menu_id>/del/menuitem/<int:menuItem_id>", views.del_menuItem, name="del_menuItem"),
    path("<int:menu_id>/new/menuitem/", views.new_menuItem, name="new_menuItem"),
    path("<int:menu_id>/detail/menuitem/<int:menuItem_id>", views.detail_menuItem, name="detail_menuItem"),

    path("page/", views.page, name="page"),
    path("del/page/<int:page_id>", views.del_page, name="del_page"),
    path("new/page/", views.new_page, name="new_page"),
    path("detail/page/<int:page_id>", views.detail_page, name="detail_page"),
]
