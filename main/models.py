from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(verbose_name="Product Category", max_length=100, unique=True, blank=False, null=False)
    def __str__(self):
        return self.category_name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, verbose_name="Product Category", related_name="products", on_delete=models.CASCADE)
    product_name = models.CharField(verbose_name="Product", max_length=100, unique=True, blank=False, null=False)
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    price = models.FloatField(verbose_name="Price", default=0.0, null=False)
    def __str__(self):
        return self.product_name


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, verbose_name="Product", related_name="details", on_delete=models.CASCADE)
    color = models.CharField(verbose_name="Product Color", max_length=50, blank=False, null=False)
    quantity = models.FloatField(verbose_name="Product Quantity", default=0.0, null=False)
    picture = models.ImageField(
        verbose_name="Image",
        upload_to="product/images/",
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])],
        blank=True, null=True
    )
    def image(self):
        return mark_safe('<img src="/../../media/%s" width="80" />' % (self.picture))

    image.allow_tags = True
    def __str__(self):
        return f"{self.product} - {self.color}"


class StockMovement(models.Model):
    class MovementType(models.TextChoices):
        STOCK_IN = "Stock In", "Stock In"
        STOCK_OUT = "Stock Out", "Stock Out"

    product_detail = models.ForeignKey(ProductDetail, verbose_name="Product", related_name="stock_movements", on_delete=models.CASCADE)
    movement_type = models.CharField(verbose_name="Movement", choices=MovementType.choices, max_length=10)
    quantity = models.FloatField(verbose_name="Product Quantity", default=0.0, null=False)
    total_price = models.FloatField(verbose_name="Total Price", default=0.0, null=False)
    processed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_detail} - {self.movement_type} - {self.quantity}"

    def save(self, *args, **kwargs):
        # Update the product_detail quantity based on the stock movement
        if self.movement_type == 'Stock In':
            self.product_detail.quantity += self.quantity
        elif self.movement_type == 'Stock Out':
            self.product_detail.quantity -= self.quantity

        # Calculate and update the total price based on the quantity and any other relevant data
        self.total_price = self.product_detail.product.price * self.quantity

        # Save the StockMovement instance and update the related ProductDetail
        super().save(*args, **kwargs)
        self.product_detail.save()
