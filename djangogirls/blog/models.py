from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# class to specjalne słowo kluczowe, które sygnalizuje, że tworzymy obiekt.
# Post to nazwa naszego modelu
# models.Model oznacza, że nasz obiekt Post jest modelem Django. W ten sposób Django wie, że powinien go przechowywać w bazie danych.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #models.CharField - tak definiujemy tekst z ograniczoną liczbą znaków.
    title = models.CharField(max_length=200)
    #models.TextField - a to nadaje się do dłuższych tekstów bez ograniczeń w ilości znaków
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #W Django każda instancja modelu (np. Post) odpowiada jednemu wierszowi w tabeli bazy danych.
    #Gdy zmieniasz coś w obiekcie (np. self.published_date = timezone.now()), to ta zmiana dzieje się tylko w pamięci — dopóki nie wywołasz save(), nic nie zapisuje się w bazie.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #The __str__() method returns a human-readable, or informal, string representation of an object. This method is called by the built-in print() , str() , and format() functions.
    def __str__(self):
        return self.title