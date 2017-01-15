from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib import messages

from .models import InventoryItem

# Create your views here.

def index(request):
    all_items = InventoryItem.objects.all()
    template = loader.get_template('inventory/index.html')
    context = {
        'all_inventory_items': all_items
    }
    return HttpResponse(template.render(context, request))


def detail(request, item_id):
    try:
        inventory_item = InventoryItem.objects.get(pk=item_id)
    except InventoryItem.DoesNotExist:
        raise Http404("Inventory Item does not exist")
    return render(request, "inventory/detail.html", {'inventory_item': inventory_item})


def new(request):
    return render(request, "inventory/new.html", {})

def newpilot(request):
    return render(request, "inventory/newpilot.html", {})
