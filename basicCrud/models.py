from django.db import models

# Create your models here.

class Item(models.Model):
    
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name