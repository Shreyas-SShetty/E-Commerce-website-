from django.shortcuts import render
from .models import Item, Buyer
from django.utils import timezone

def home_page(request) :
    items = Item.objects.order_by('name')
    return render(request, 'blog/home_page.html', {'items' : items})

