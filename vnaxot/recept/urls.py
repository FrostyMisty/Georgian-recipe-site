from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:pk>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('about-us/', views.about_us, name='about_us'),
    path('about-georgia/', views.about_georgia, name='about_georgia'),
    path('contact-us/', views.contact_us, name='contact_us'),
    # ...other patterns...
]
