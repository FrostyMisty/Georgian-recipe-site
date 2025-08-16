from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
