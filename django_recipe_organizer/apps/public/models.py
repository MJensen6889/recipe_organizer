from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ingredients = models.ManyToManyField('Ingredient')
    categories = models.CharField(max_length=50, default="No category has been entered yet.")
    rating = models.IntegerField(blank=True, null=True)
    description = models.TextField(default="No description has been entered yet.")
    instructions = models.TextField(default="No instructions have been added yet.")
    photo = models.CharField(max_length=10000, blank=True, null=True)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name