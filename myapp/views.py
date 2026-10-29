from django.http import HttpResponse
from django.shortcuts import render

from myapp.models import Item

# Create your views here.

def index(request):
    items_list = Item.objects.all()
    context = {
        'items_list': items_list
    }
    return render(request, 'myapp/index.html', context)

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    return HttpResponse(f"details view for item {item.name} with id {item_id}")

def home(request):
    return HttpResponse("second view.")
