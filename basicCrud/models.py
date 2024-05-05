from django.db import models

# Create your models here.


class MyItem(models.Model):

    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50, null=True)
    owner = models.CharField(max_length=50, null=True)
    created_at = models.DateField(auto_now_add=True)
    expiry_data = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
