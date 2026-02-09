from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies

# Create your views here.
def home(request):
   searchTem =  request.GET.get('searchMovie')
   if searchTem:
       movies = Movies.objects.filter(title__icontains=searchTem)
   else: 
       movies = Movies.objects.all
   return render(request, 'home.html', {'searchTerm': searchTem, 'movies': movies})


def about(request):
    return render(request, 'about.html')