from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Announce
from .services.avito import get_page_content
# Create your views here.


def mainapp(request):
    all_ad = Announce.objects.all()
    context = {
        'ads': all_ad,
    }
    return render(request, 'index.html', context)


def refresh_db(request):
    get_page_content()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
