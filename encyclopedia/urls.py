from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new/", views.create, name="create"),
    path("edit/", views.edit, name='edit'),
    path("save_it/", views.save_it, name='save_it'),
    path("random_page/", views.random_page, name='random_page')
]
