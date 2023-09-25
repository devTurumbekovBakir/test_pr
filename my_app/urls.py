from django.urls import path
from . import views

urlpatterns = [
    path('create_author/', views.create_author, name='create_author'),
    path('create_book/<int:author_id>/', views.create_book, name='create_book'),

]
