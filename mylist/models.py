from django.db import models
from datetime import date

# Create your models here.
# python manage.py makemigrations
# python manage.py migrate
# ca min 53

class ShoppingItem(models.Model):
    created_at = models.DateField(default=date.today)
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) + " " + self.name