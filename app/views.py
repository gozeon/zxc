from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Application, Page


@login_required
def index(request):
    result = Application.objects.filter(pub_date__isnull=False,
                                        create_user__isnull=False,
                                        delete_date__isnull=True).order_by('-pub_date')
    context = {
        "apps": result
    }
    return render(request, "app/index.html", context)


@login_required
def detail(request, app_id):
    context = {}
    app = get_object_or_404(Application, pk=app_id)
    context["app"] = app

    page_id = request.GET.get("pageId")
    if page_id:
        page = get_object_or_404(Page, pk=page_id)
        context["page"] = page

    return render(request, "app/detail.html", context)
