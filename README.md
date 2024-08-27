In Django, a ViewSet is a class that combines the logic for handling multiple actions, such as list, create, retrieve, update, and delete (CRUD operations) for a specific model or resource in a single class. ViewSets are commonly used with Django Rest Framework (DRF) to create APIs efficiently.

#There are different types of ViewSets:

-    ModelViewSet: This is the most commonly used ViewSet in DRF, providing complete CRUD functionality. It automatically includes actions for listing, retrieving, creating, updating, and deleting objects.

-    ReadOnlyModelViewSet: This is a ViewSet that provides only the list and retrieve actions, meaning it’s read-only.

-    GenericViewSet: A base class that can be used if you want to define your own combination of actions (e.g., you want some but not all CRUD operations).

===========================================================================================================================================    
  #example:
  
  ##"modelviewset"

  from rest_framework import viewsets
  from .models import Movie
  from .serializers import MovieSerializer

  class MovieViewSet(viewsets.ModelViewSet):
      queryset = Movie.objects.all()  # Define the queryset for the ViewSet
      serializer_class = MovieSerializer  # Specify the serializer class
===================================================================
 ## Example of using ReadOnlyModelViewSet
 from rest_framework import viewsets
 from .models import Movie
 from .serializers import MovieSerializer

class MovieReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

===================================================================
##Routing ViewSets

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)  # Register the ViewSet

urlpatterns = [
      path('', include(router.urls)),
]

 

  
