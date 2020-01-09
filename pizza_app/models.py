from django.db import models
from django.utils import timezone
from typing import List


class OptionGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Option(models.Model):
    option_group = models.ForeignKey(
        OptionGroup, related_name="options", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title}:{self.price}"


class ToppingGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Topping(models.Model):
    topping_group = models.ForeignKey(
        ToppingGroup, related_name="toppings", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.title}:{self.price}"


class Order(models.Model):
    customer_name = models.CharField(max_length=100, default="")
    customer_email = models.EmailField(max_length=100, default="")
    customer_phone_number = models.CharField(max_length=15, default="")
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def price(self):
        """ Returns the price of the order. """
        total_price = 0
        order_options: List[OrderOption] = self.__getattribute__(
            "option").all()
        for order_option in order_options:
            total_price += order_option.price

        order_toppings: List[OrderTopping] = self.__getattribute__(
            "topping").all()
        for order_topping in order_toppings:
            total_price += order_topping.price

        return total_price

    def __str__(self):
        return f"Total price: {self.price} by {self.customer_name}"


class OrderOption(models.Model):
    order = models.ForeignKey(
        Order, related_name="option", on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    @property
    def price(self):
        return self.option.price

    def __str__(self):
        return f"{self.option.title}, price: {self.price}"


class OrderTopping(models.Model):
    order = models.ForeignKey(
        Order, related_name="topping", on_delete=models.CASCADE)
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)
    amount = models.IntegerField()

    @property
    def price(self):
        return self.topping.price * self.amount

    def __str__(self):
        return f"{self.topping.title}, amount: {self.amount}"
