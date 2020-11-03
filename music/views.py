#from django.shortcuts import render
from django.http import Http404
#from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader
from .models import Album

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', context)

     # all_albums = Album.objects.all()
     # #By default Django looks in the templates directory
     # template = loader.get_template('music/index.html')
     # context = {'all_albums' : all_albums}
     # return HttpResponse(template.render(context, request))

    # all_albums = Album.objects.all()
    # html = ''
    # for album in all_albums:
    #     url = '/music/'+ str(album.id) +'/'
    #     html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
    # return HttpResponse(html)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})
    #return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
