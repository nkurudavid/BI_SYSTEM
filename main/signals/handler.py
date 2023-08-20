from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from main.models import ProductDetail, Order, OrderDetail, StockMovement


@receiver(post_save, sender=Order)
def update_stock_on_order_success(sender, instance, **kwargs):
    if instance.status == Order.OrderStatus.SUCCESS:
        for order_detail in instance.order_details.all():
            product_detail = order_detail.product_detail
            quantity = order_detail.quantity

            if order_detail.product_detail.quantity >= quantity:
                # Reduce stock for stock out
                product_detail.quantity -= quantity
                product_detail.save()

                # Record stock movement
                StockMovement.objects.create(
                    product_detail=product_detail,
                    movement_type=StockMovement.MovementType.STOCK_OUT,
                    quantity=quantity,
                    total_price=quantity * order_detail.product_detail.product.price,
                    processed_by=instance.client,
                )

# Connect the signal handler function to the post_save signal of the Order model
post_save.connect(update_stock_on_order_success, sender=Order)


@receiver(post_save, sender=ProductDetail)
def record_stock_movement(sender, instance, created, **kwargs):
    if created:
        # If a new ProductDetail instance is created, record a Stock In movement
        StockMovement.objects.create(
            product_detail=instance,
            movement_type=StockMovement.MovementType.STOCK_IN,
            quantity=instance.quantity,
            total_price=instance.product.price * instance.quantity,
            processed_by=None  # Set the processed_by user as needed
        )
    else:
        # If an existing ProductDetail instance is updated, calculate the quantity change
        old_instance = ProductDetail.objects.get(pk=instance.pk)
        quantity_change = instance.quantity - old_instance.quantity

        if quantity_change > 0:
            # If quantity increased, record a Stock In movement
            movement_type = StockMovement.MovementType.STOCK_IN
        elif quantity_change < 0:
            # If quantity decreased, record a Stock Out movement
            movement_type = StockMovement.MovementType.STOCK_OUT
        else:
            # Quantity didn't change, no need to record a movement
            return

        StockMovement.objects.create(
            product_detail=instance,
            movement_type=movement_type,
            quantity=abs(quantity_change),
            total_price=instance.product.price * abs(quantity_change),
            processed_by=None  # Set the processed_by user as needed
        )
