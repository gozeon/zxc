from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Application, Page


@login_required
def index(request):
    result = Application.objects.filter(pub_date__isnull=False,
                                        create_user__isnull=False).order_by('-pub_date')
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

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.findAll('link')
        for link in links:
            link.extract()

        context['links'] = ''.join(str(l) for l in links)
        print(links)
        styles = soup.findAll('style')
        for style in styles:
            style.extract()
        context['styles'] = ''.join(str(l) for l in styles)

        scripts = soup.findAll('script')
        for script in scripts:
            script.extract()
        context['scripts'] = ''.join(str(l) for l in scripts)

        context['elements'] = str(soup)

    return render(request, "app/detail.html", context)
