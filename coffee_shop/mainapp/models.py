from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Product Name")
    price = models.PositiveIntegerField(verbose_name="Price (₹)")
    desc = models.TextField(verbose_name="Description")
    pic = models.ImageField(upload_to="products/", verbose_name="Product Image")
    stock = models.PositiveIntegerField(default=1, verbose_name="Stock Quantity")

    def __str__(self):
        return self.name  # Returns product name in the Django admin panel and queries
