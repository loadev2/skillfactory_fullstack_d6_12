from catalog.views import index, dogs, cats, parrots, contacts, pet
from django.urls import path

app_name = 'catalog'
urlpatterns = [
    path('', index, name='index'),
    path('index.html/', index, name='index'),
    path('dogs/', dogs, name='dogs'),
    path('cats/', cats, name='cats'),
    path('pet/<str:id>', pet, name="pet"),
    path('parrots/', parrots, name='parrots'),
    path('contacts/', contacts, name="contacts")
]

