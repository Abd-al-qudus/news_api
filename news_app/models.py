from django.db import models

# Create your models here.


class Author(models.Model):
    "author models"

    full_name = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=False)
    email = models.EmailField(max_length=100, null=False)
    contact = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.full_name}"


class News(models.Model):
    """a model for the news class"""

    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=100)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    body = models.TextField(null=False)
    
    def __str__(self):
        return f"{self.title}"
