import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
