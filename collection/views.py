from django.shortcuts import render
from collection.models import Episode
# Create your views here.

def index(request):
    episodes = Episode.objects.all()
    return render(request, 'index.html', { 
        'episodes' : episodes 
    })