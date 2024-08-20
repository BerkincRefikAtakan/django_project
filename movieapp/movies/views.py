from django.shortcuts import render
from .models import Category,Movie
# Create your views here.


def home(request):
    data={
        "kategori_list": Category.objects.all(),
        "film_list": Movie.objects.filter(anasayfa=True)
    }
    return render(request,"index.html",data)

def movies(request):
    data={
        "kategori_list": Category.objects.all(),
        "film_list": Movie.objects.all()
    }
    return render(request,"movies.html",data)


def moviedetails(request,id):
    data={
        "movie":Movie.objects.get(id=id)
    }
    return render(request,"details.html",data)