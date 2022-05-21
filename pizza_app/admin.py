from django.contrib import admin
from .models import ToppingGroup, Topping, OptionGroup, Option, Order, OrderOption, OrderTopping

admin.site.register([ToppingGroup, Topping, OptionGroup, Option, Order, OrderOption, OrderTopping])
