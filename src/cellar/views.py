from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Wines, Inventory

@login_required
def index(request):

    # Vulnerability: A01:2021-Broken Access Control
    # Any user can see the inventory of anyone
    # So it must be fixed so that users only have access to their own inventories
    # The fix is to change the line to this: user_inventory = Inventory.objects.filter(owner=request.user)

    user_inventory = Inventory.objects.all()

    all_wines = Wines.objects.all()
    context = {
        "user_inventory": user_inventory,
        "all_wines": all_wines
    }
    return render(request, "cellar/index.html", context)


#A07:2021-Identification and Authentication Failures
# @login_required is missing meaning that non users that aren't Authentication can request this route
# This can cause lead to exploits or bugs (like anyone spamming the database)
# the fix is to add @login_required before this view

def add_to_inventory(request):
    if request.method == 'POST':
        wine_id = request.POST.get('wine_id')
        quantity = request.POST.get('quantity')
        
        wine = Wines.objects.get(id=wine_id)
        
        existing_inventory, created = Inventory.objects.get_or_create(
            owner=request.user,
            wine_id=wine,
            defaults={'quantity': quantity}
        )
        
        if not created:
            existing_inventory.quantity += int(quantity)
            existing_inventory.save()
        
        return redirect('index') 
    
    return redirect('index')  