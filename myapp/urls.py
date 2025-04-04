from django.urls import path 
from .views import main, author, fishshop

urlpatterns = [
    path('', main, name = 'main'),
    path('author', author,name= 'author'),
    path('fishshop', fishshop,name= 'fishshop')
]