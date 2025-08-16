from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm

def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form, 'edit': True})

def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})

def recipe_search(request):
    query = request.GET.get('q', '')
    recipes = Recipe.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    ) if query else Recipe.objects.none()
    return render(request, 'recipe_search.html', {'recipes': recipes, 'query': query})

def about_us(request):
    return render(request, 'about_us.html')

def about_georgia(request):
    return render(request, 'about_georgia.html')

def contact_us(request):
    return render(request, 'contact_us.html')
