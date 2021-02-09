from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(entry)
    })

def new(request):
    return render(request, "encyclopedia/new.html")

def random(request):
    return render(request, "encyclopedia/random.html")