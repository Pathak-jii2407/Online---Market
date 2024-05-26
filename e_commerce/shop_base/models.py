from django.db import models
from django.contrib.auth.models import User

class Cloth(models.Model):
    id = models.AutoField(primary_key=True, serialize=False)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Changed to DecimalField for better precision
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Review(models.Model):
    clothes = models.ForeignKey(Cloth, related_name='reviews', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} for {self.clothes.name}"

class BuyProduct(models.Model):
    clothes = models.ForeignKey(Cloth, related_name='purchases', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='purchases', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase of {self.clothes.name} by {self.user.username}"
