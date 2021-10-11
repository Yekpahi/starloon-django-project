from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Person
import json
# Create your views here.

def index(request) :
    person_objects = Person.objects.all()
    user = request.user
    paginator = Paginator(person_objects, per_page=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request,'home/home.html', {
      'person_objects': page_obj.object_list,
      'paginator' : paginator,
      'page_number':int(page_number),
      'user' : user
      })

def searchBar(request):
    if request.method == "GET":
        query = request.GET.get("query")
        if query:
            persons = Person.objects.filter(Q(fullName=query) | Q(surname=query))
            return render(request, "home/home.html", {'persons' : persons})
        else:
            print("No information to show")
            return request(request, 'home/home.html')


def detail(request, slug) :
    person = Person.objects.get(slug=slug)
    context = {
     'person': person
    }
    return render(request, 'details/details.html', context)