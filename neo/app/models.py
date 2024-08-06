from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models. DateField (null=True, blank=True)
 
class Book(models.Model):
    title = models.CharField(max_length=255)  
    author = models.ForeignKey(Author,max_length=255, default="", blank=True, on_delete=models.CASCADE)  
    summary = models.TextField(null=True, blank=True)  
    isbn = models.CharField(max_length=255, unique=True)
 
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)   

class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('m', 'Maintenant disponible'),
        ('o', 'En cours de prêt'),
        ('r', 'Réservé'),
        ('a', 'Maintenance'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    imprint = models.CharField(max_length=200)  
    due_back = models.DateField()  
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,
        default='m',)
