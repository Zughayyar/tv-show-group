from django.shortcuts import render, redirect, HttpResponse
from . import models

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : models.get_all_shows()
    }
    return render(request ,"shows.html", context)

def addShow(request):
    return render(request, "showAdd.html")

def createShow(request):
    if request.method == "POST":
        models.create_show(request.POST)
        return redirect('/shows')


    else:
        return HttpResponse("Soemthing wrong!")

def showID(request, id):
    context = {
        'show' : models.get_show_by_id(id)
    }
    return render(request, "show_id.html", context)

def deleteShow(request, id):
    models.delete_show(id)
    return redirect('/shows')