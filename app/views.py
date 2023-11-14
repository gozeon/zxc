from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Application


@login_required
def index(request):
    result = Application.objects.filter(pub_date__isnull=False,
                                        create_user__isnull=False,
                                        create_user=request.user).order_by('-pub_date')
    context = {
        "apps": result
    }
    return render(request, "app/index.html", context)


def detail(request, app_id):
    app = get_object_or_404(Application, pk=app_id)
    context = {
        "app": app
    }
    return render(request, "app/detail.html", context)
