from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Person
import json
# Create your views here.

def index(request) :
    person_objects = Person.objects.all()

    # Search funtionality
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:                             #For querysets questions please view the page
        person_objects =Person.filter(first_name__icontains = item_name) #https://sodocumentation.net/django/topic/1235/querysets
    paginator = Paginator(person_objects, per_page=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request,'home/home.html', {
      'person_objects': page_obj.object_list,
      'paginator' : paginator,
      'page_number':int(page_number),
      })

def detail(request, slug) :
    person = person.objects.get(slug=slug)

    context = {
     'person': person
    }
    return render(request, 'details/details.html', context)
