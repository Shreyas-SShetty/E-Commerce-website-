from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item, Buyer
from .forms import ItemForm
from django.utils import timezone

def home_page(request) :
    items = Item.objects.order_by('name')
    return render(request, 'blog/home_page.html', {'items' : items})

def item_page(request, pk) :
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'blog/item_page.html', {'item' : item})

def item_new(request) :
    form = ItemForm()
    return render(request, 'blog/home_page.html', {'form' : form})


