from django.shortcuts import render
# Import des Datenbankmodels 
from .models import ShoppingItem
# Create your views here.

def mylist(request):
    #Annahme aus FormData im Backend
    if request.method == 'POST':
        print('Received data: ', request.POST['itemName'])
        #Zeile in DB hinzufügen
        ShoppingItem.objects.create(name = request.POST['itemName'])
    
    # Darstellung aller Objekte der Datenbank
    all_items = ShoppingItem.objects.all()
    
    #Darstellung
    return render(request, 'shopping_list.html', {'all_items': all_items})