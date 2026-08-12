from django.db import models

class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"