from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from .forms import movieform
# Create your views here.
def index(request):
    mv=movie.objects.all
    context={
        'movie_list':mv
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    mv=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':mv})
def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        Movie= movie(name=name ,desc=desc,year=year,img=img)
        Movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':Movie})
def delete(request,id):
    if request.method=='POST':
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,'delete.html')