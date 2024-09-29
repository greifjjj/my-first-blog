from django.shortcuts import render
from .models import Book
import json


def import_data(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        for item in data:
            book = Book(
                title=item['title'],
                author=item['author'],
                publication_year=item['publication_year']
            )
            book.save()
        return render(request, 'success.html')
    return render(request, 'form.html')