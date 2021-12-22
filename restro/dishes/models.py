from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural="Category"
        
    def __str__(self):
            return self.name
       
class Dish(models.Model):
    name=models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    cost = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural="Dish"
    
    def __str__(self):
        return f"{self.name} {self.id}({self.rating})"
    
class Chef(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),         
                                   
        ('Female', 'Female'),

    )
    first_name=models.CharField(max_length=255)
    age=models.IntegerField(default=1)
    gender=models.CharField(max_length=100, choices=GENDER_CHOICES)
    dishes=models.ManyToManyField(Dish)
    
    class Meta:
        verbose_name_plural="Chef"
    
    def __str__(self):
        return f"{self.first_name}"



    
    
        
