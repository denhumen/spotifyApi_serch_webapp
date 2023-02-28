from django.shortcuts import render
from django.template import RequestContext
from main.scripts import search_artist
import folium as fl
from main.scripts import search_artist

# Create your views here.
def index(request):
    """
    Function
    """
    if request.method == 'POST':
        try:
            input_text = request.POST.get('button')
            token = search_artist.get_token()
            result = search_artist.search_for_artist(token, input_text)
            if result == None:
                return render(request, 'main/notfound_artist.html')
            artist_name = result["name"]
            tmp_song = search_artist.get_songs_by_artist(token, result["id"])[0]['name']
            search_artist.create_map(artist_name)
            return render(request, 'main/loading.html', {"artist_name":artist_name, "tmp_song":tmp_song})
        except Exception:
            return render(request, 'main/notfound_artist.html')
    return render(request, 'main/search_page.html')

def shopwmap(request):
    """
    Function
    """
    return render(request, 'main/map.html', {})

def notfound(request):
    return render(request, 'main/notfound_artist.html')
