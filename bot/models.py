from itertools import filterfalse

from django.utils import timezone
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bg/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Museum(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


# New model for storing multiple images for each museum


class Category(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'Adult', 'Child', 'Photograph'
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name


class Price(models.Model):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name='prices')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price for this category

    def __str__(self):
        return f'{self.category.name} - {self.museum.name} - ${self.price}'


class Ticket(models.Model):
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name='tickets')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tickets')
    customer_name = models.CharField(max_length=100)
    customer_age = models.IntegerField(default=0)
    customer_email = models.EmailField()
    customer_phoneno = models.BigIntegerField( null=False, blank=False, default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # This will be set based on the category

    def save(self, *args, **kwargs):
        # Set the price based on the selected category
        if self.category:
            try:
                price_record = Price.objects.get(museum=self.museum, category=self.category)
                self.price = price_record.price
            except Price.DoesNotExist:
                self.price = 0  # Or handle the case where no price is set
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Ticket for {self.museum.name} - {self.customer_name} - ${self.price}'

    def __str__(self):
        return f'Ticket for {self.museum.name} - {self.customer_name}'


class MuseumImage(models.Model):
    museum = models.ForeignKey(Museum, related_name='images', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='images', blank=True, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='images', blank=True, null=True)

    image = models.ImageField(upload_to='museum_images/')  # Folder to store images

    def __str__(self):
        return f"{self.museum.name} - Image"
