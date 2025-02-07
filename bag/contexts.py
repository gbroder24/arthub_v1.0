from django.conf import settings
from decimal import Decimal


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    discount_percentage = 0

    # Apply % discount to the total
    discount_percentage = settings.DISCOUNT_PERCENTAGE  # % discount
    total_with_discount = total * Decimal(1 - discount_percentage / 100)

    if total_with_discount < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total_with_discount * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        free_delivery_delta = (
            settings.FREE_DELIVERY_THRESHOLD - total_with_discount
            )
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total_with_discount

    context = {
        'bag_items': bag_items,
        'total': total_with_discount,  # Updated total after discount
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
