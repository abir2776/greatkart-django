from atexit import register
from django import template
from app_booking.models import Bookings

register = template.Library()

@register.filter
def cart_total(user):
    order = Bookings.objects.filter(user=user,ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0