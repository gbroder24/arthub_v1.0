from django import template
from decimal import Decimal


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(product, quantity):
    # Apply discount to the product price
    discounted_price = product.price * Decimal(
        1 - product.discount_percentage / 100
        )
    return discounted_price * quantity
