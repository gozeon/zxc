from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from app.models import Application


@login_required
def index(request):
    return render(request, "dash/index.html")


@login_required
def app(request):
    if request.method == 'GET':
        apps = Application.objects.filter(create_user__isnull=False,
                                          delete_date__isnull=True).order_by('-create_date')
        return render(request, "dash/app.html", {
            "apps": apps
        })

    return render(request, "dash/index.html")


@login_required
def del_app(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    app.delete_date = datetime.now()
    app.save()
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
