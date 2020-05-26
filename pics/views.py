from django.shortcuts import render
from .models import Picture

# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    return render(request,'index.html',{"pictures":pictures})

def search_results(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_Pictures = Picture.search_by_description(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message": message,"Pictures": searched_Pictures})

    else:
        message = " Nothing was found. Please try again."
        return render(request,'search.html',{"message":message})

def search_location(request,location):
    pictures_by_location = Picture.filter_by_location(location)

    return render(request,'location.html',{"pictures":pictures_by_location})

def search_picture(request,pic):
    pictures_by_location = Picture.get_picture_by_id(pic)

    return render(request,'location.html',{"pictures":pictures_by_location})

