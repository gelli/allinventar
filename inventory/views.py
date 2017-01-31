from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.contrib import messages

from .models import InventoryItem
from .models import MaterialGroup

from .forms import NewEinzelbuchungForm


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
    if request.method == 'POST':
        form = NewEinzelbuchungForm(request.POST)
        if form.is_valid():
            print("form is valid")
            return HttpResponseRedirect('/inventory/')
    else:
        form = NewEinzelbuchungForm()

    return render(request, 'inventory/new.html', {'form': form})


def newpilot(request):
    return render(request, "inventory/newpilot.html", {})
