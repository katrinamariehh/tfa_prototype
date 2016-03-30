from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=350)

    def __str__(self):
        return self.title
