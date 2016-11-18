from django.db import models

from cellphones.models import Device, DeviceAccessories
from django.contrib.auth.models import User

from .helpers import *
from django.core.validators import RegexValidator


# Create your models here.

class Customer(models.Model):
    """add more user detail into User auth"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=300, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, choices=CITIES, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=300, null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer)

    items = models.ManyToManyField(Device,through="OrderItem")

    original_price = models.FloatField(null=True,blank=True)
    deduction = models.FloatField(default=0)
    delivered_cost = models.FloatField(null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)    #last value

    checkout_date = models.DateTimeField()
    delivering_estimate_date = models.DateField(blank=True, null=True)
    delivered_date = models.DateTimeField(blank=True, null=True)

    payment_type = models.SmallIntegerField(choices=PAYMENT_TYPE, null=True, blank=True)
    num_regex = RegexValidator(regex=r'^\d{16}$',
                                 message="Card number must be entered numeric only")
    card_number = models.CharField(validators=[num_regex],blank=True, null=True, max_length=16)

    shipping_address = models.TextField(blank=True, null=True)

    description = models.TextField(max_length=500)
    CART_STATUS = (
        (1, "SHOPPING"),   # which refer to CART
        (2, "CHECK OUT"),  # wait for employer process
        (3, "ON DELIVER"),
        (4, "DELIVERED"),
        (5, "CANCELLED"),
        (6, "RETURNING"),
        (7, "RETURNED"),
        (8, "INACTIVE"),
    )
    order_status = models.SmallIntegerField(choices=CART_STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # @classmethod
    # def get_cart(cls, user, id=None):
    #     if not id:
    #         cart = cls(user=user)
    #         return cart
    #     else:
    #         self.





class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    item = models.ForeignKey(Device)
    quantity = models.IntegerField(default = 1)
    price = models.FloatField()             # current price
    original_price = models.FloatField()    # original price
    discounted_price = models.FloatField(null=True, blank=True)