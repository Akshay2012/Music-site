from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import album,song
from django.template import loader
# Create your views here.

def index(request):
    all_albums=album.objects.all()
    context={
        'all_albums':all_albums
    }
    return render(request,'music/index.html',context=context)
    
def detail(request,album_id):
    try:
        alb=album.objects.get(pk=album_id)
    except album.DoesNotExist:
        raise Http404("Album does not exist")
    
    return render(request,'music/detail.html',{'albums':alb})
