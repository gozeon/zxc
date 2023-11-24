from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt

from app.models import Application, Menu, MenuItem, Page
from .forms import AppForm, MenuForm, PageForm, MenuItemForm


@login_required
def index(request):
    app_count = Application.objects.all().count()
    menu_count = Menu.objects.all().count()
    page_count = Page.objects.all().count()
    return render(request, "dash/index.html", {
        "app_count": app_count,
        "menu_count": menu_count,
        "page_count": page_count,
    })


@login_required
def app(request):
    apps = Application.objects.filter(create_user__isnull=False,
                                      delete_date__isnull=True).order_by('-create_date')
    return render(request, "dash/app/app.html", {
        "apps": apps
    })


@login_required
def new_app(request):
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            app = form.save(commit=False)
            app.create_user = request.user
            app.save()
            messages.success(request, "Create {} Success".format(app.name))
            return HttpResponseRedirect(reverse('dash:app'))
    else:
        form = AppForm()
    return render(request, "dash/app/create.html", {"form": form})


@login_required
def detail_app(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    if request.method == 'POST':
        form = AppForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            messages.success(request, "Update {} Success".format(app.name))
            return HttpResponseRedirect(reverse('dash:app'))
    else:
        form = AppForm(instance=app)
    return render(request, "dash/app/detail.html", {"form": form})


@login_required
def del_app(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    # app.delete_date = datetime.now()
    # app.save()
    app.delete()
    messages.success(request, "Delete {} Success".format(app.name))
    return HttpResponseRedirect(reverse('dash:app'))


@login_required
def pub_app(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    action = "Publish"
    if app.pub_date is None:
        app.pub_date = datetime.now()
    else:
        app.pub_date = None
        action = "UnPublish"
    app.save()
    messages.success(request, "{} {} Success".format(action, app.name))
    return HttpResponseRedirect(reverse('dash:app'))


@login_required
def menu(request):
    if request.method == 'GET':
        menus = Menu.objects.filter(delete_date__isnull=True).order_by('-create_date')
        return render(request, "dash/menu/menu.html", {
            "menus": menus
        })

    return render(request, "dash/index.html")


@login_required
def new_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.create_user = request.user
            menu.save()
            messages.success(request, "Create {} Success".format(menu.name))
            return HttpResponseRedirect(reverse('dash:menu'))
    else:
        form = MenuForm()
    return render(request, "dash/menu/create.html", {"form": form})


@login_required
def detail_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, "Create {} Success".format(menu.name))
            return HttpResponseRedirect(reverse('dash:menu'))
    else:
        form = MenuForm(instance=menu)
    return render(request, "dash/menu/detail.html", {"form": form, "menuId": menu_id})


@login_required
def del_menu(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    # menu.delete_date = datetime.now()
    # menu.save()
    menu.delete()
    messages.success(request, "Delete {} Success".format(menu.name))
    return HttpResponseRedirect(reverse('dash:menu'))


@xframe_options_exempt
@login_required
def menuItem(request, menu_id):
    if request.method == 'GET':
        menuItems = MenuItem.objects.filter(delete_date__isnull=True, menu_id=menu_id).order_by('-create_date')
        return render(request, "dash/menu/menuItem/menuItem.html", {
            "menuItems": menuItems,
            "menuId": menu_id
        })

    return render(request, "dash/index.html")


@xframe_options_exempt
@login_required
def new_menuItem(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menuItem = form.save(commit=False)
            menuItem.menu = menu
            menuItem.save()
            messages.success(request, "Create {} Success".format(menu.name))
            return HttpResponseRedirect(reverse('dash:menuItem', kwargs={"menu_id": menu_id}))
    else:
        form = MenuItemForm()
    return render(request, "dash/menu/menuItem/create.html", {"form": form, "menuId": menu_id})


@xframe_options_exempt
@login_required
def detail_menuItem(request, menu_id, menuItem_id):
    menuItem = get_object_or_404(MenuItem, pk=menuItem_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=menuItem)
        if form.is_valid():
            form.save()
            messages.success(request, "Update {} Success".format(menu.name))
            return HttpResponseRedirect(reverse('dash:menuItem', kwargs={"menu_id": menu_id}))
    else:
        form = MenuItemForm(instance=menuItem)
    return render(request, "dash/menu/menuItem/detail.html", {"form": form, "menuId": menu_id})


@xframe_options_exempt
@login_required
def del_menuItem(request, menu_id, menuItem_id):
    menuItem = get_object_or_404(MenuItem, pk=menuItem_id, menu_id=menu_id)
    # menuItem.delete_date = datetime.now()
    # menuItem.save()
    menuItem.delete()
    messages.success(request, "Delete {} Success".format(menuItem.name))
    return HttpResponseRedirect(reverse('dash:menuItem', kwargs={"menu_id": menu_id}))


@login_required
def page(request):
    if request.method == 'GET':
        pages = Page.objects.filter(delete_date__isnull=True).order_by('-create_date')
        return render(request, "dash/page/page.html", {
            "pages": pages
        })

    return render(request, "dash/index.html")


@login_required
def new_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.create_user = request.user
            page.save()
            messages.success(request, "Create {} Success".format(page.name))
            return HttpResponseRedirect(reverse('dash:page'))
    else:
        form = PageForm()
    return render(request, "dash/page/create.html", {"form": form})


@login_required
def detail_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            messages.success(request, "Update {} Success".format(page.name))
            return HttpResponseRedirect(reverse('dash:page'))
    else:
        form = PageForm(instance=page)
    return render(request, "dash/page/detail.html", {"form": form})


@login_required
def del_page(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    page.delete_date = datetime.now()
    page.save()
    # page.delete()
    messages.success(request, "Delete {} Success".format(page.name))
    return HttpResponseRedirect(reverse('dash:page'))
