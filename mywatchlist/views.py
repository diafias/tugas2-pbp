from email import message
from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_mywatchlist(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_film': data_film_mywatchlist,
        'nama': 'Diah Afia Safitri'
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    data_film_mywatchlist = MyWatchList.objects.all()
    watched = 0
    not_watched = 0
    for film in data_film_mywatchlist:
        if film.watched :
            watched = watched + 1
        else :
            not_watched = not_watched + 1
        
    if watched > not_watched:
        message = "Selamat kamu sudah banyak menonton anime"
    else :
        message = "kamu masih kurang menonton anime"
    context = {
        'list_film': data_film_mywatchlist,
        'message' : message
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
