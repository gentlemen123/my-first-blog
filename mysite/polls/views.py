from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import datetime
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def current_time(request):
    now = datetime.datetime.now()
    html = '<html><body>It is now %s .</body></html>' % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
