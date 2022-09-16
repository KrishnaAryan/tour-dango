from urllib import response
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    photo=Photo.objects.all()
    context={'photo':photo,}
    return render(request,'index.html',context)

# search 
def search(request):
    q=request.GET['q']
    photo=Photo.objects.filter(location__contains=q )
    context={'photo':photo,} 
    return render(request,'search.html',context)