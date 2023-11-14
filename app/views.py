from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Application


@login_required
def index(request):
    result = Application.objects.filter(pub_date__isnull=False, create_user__isnull=False,
                                        create_user=request.user).order_by('-pub_date')
    return HttpResponse(result)
