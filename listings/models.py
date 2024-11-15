from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    category = models.CharField(choices=[('BUY', 'Buy'), ('SELL', 'Sell'), ('RENT', 'Rent')], max_length=10)
    location = models.CharField(max_length=255)  # Add this field
    area = models.IntegerField()  # Add this field
    bedrooms = models.IntegerField()  # Add this field
    bathrooms = models.IntegerField()  # Add this field
    features = models.TextField(blank=True, null=True)  # Add this field
    image = models.ImageField(upload_to='property_images/')
    created_at = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class ChatMessage(models.Model):
    user_name = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}: {self.message[:50]}..."