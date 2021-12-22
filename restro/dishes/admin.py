from django.contrib import admin
from .models import Category,Dish,Chef

admin.site.register(Category)
admin.site.register(Dish)
class DishAdmin(admin.ModelAdmin):
    model=Dish
    list_display=[
        'id',
        'name',
        ]    
admin.site.register(Chef)

