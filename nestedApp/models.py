from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    ratings = models.CharField(max_length=10)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)