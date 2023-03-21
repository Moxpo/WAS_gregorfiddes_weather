from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.DateField()
    text = models.TextField()

# Create your models here.
