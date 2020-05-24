from django.shortcuts import render
from .models import Picture

# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    return render(request,'index.html',{"pictures":pictures})

def search_results(request):
    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_Pictures = Picture.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message": message,"Pictures": searched_Pictures})

    