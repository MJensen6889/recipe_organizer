from django.shortcuts import render
from serializers import *
from rest_framework import generics
# Create your views here.


class RecipeList(generics.ListCreateAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Recipe
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class IngredientList(generics.ListCreateAPIView):
    model = Ingredient
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class AddRecipe(generics.CreateAPIView):
    model = Recipe
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()



