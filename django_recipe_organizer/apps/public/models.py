from django.db import models

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    # ingredient_quantities = models.ManyToManyField('Ingredient_Quantity')  HOW TO DO THIS?
    ingredients = models.ManyToManyField('Ingredient')
    categories = models.CharField(max_length=50)
    description = models.TextField()
    instructions = models.TextField()

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name