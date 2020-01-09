from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Option, OptionGroup, Topping, ToppingGroup, Order, OrderOption, OrderTopping
from .forms import OrderForm


@csrf_protect
def home(request):
    if request.method == "POST":
        order = Order()
        # Otherwise save() prohibited to prevent data loss '.
        order.save(force_insert=True)
        for key, value in request.POST.items():
            if key == "Size" or key == "Crust":
                option = Option.objects.get(title=value)
                OrderOption.objects.create(order=order, option=option)
            if value.isdigit():
                topping = Topping.objects.get(title=key)
                amount = int(value)
                OrderTopping.objects.create(
                    order=order, topping=topping, amount=amount)

        return redirect('order', order_id=order.pk)
    else:
        context = {
            "option_groups": OptionGroup.objects.all(),
            "topping_groups": ToppingGroup.objects.all(),
        }
        return render(request, 'pizza_app/home.html', context)


@csrf_protect
def order(request, order_id):
    customer_order = get_object_or_404(Order, pk=order_id)
    order_price = customer_order.price
    order_time = customer_order.created_at
    order_options = OrderOption.objects.filter(order=customer_order)
    order_toppings = OrderTopping.objects.filter(order=customer_order)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_order = form.save()
            customer_order.save()
            customer_name = customer_order.customer_name
            customer_email = customer_order.customer_email

            subject = f"Order №{order_id}"
            message = f"Your ordered a pizza at {order_time}\n\n"
            message += f"For a total price of {order_price}$\n"
            message += "You choosed: \n"
            for order_option in order_options:
                message += f" - {order_option.option.title}: { order_option.price }$\n"
            for order_topping in order_toppings:
                message += f" - {order_topping.topping.title}: { order_topping.amount }00 grams\n"
            message += "Your order is ready. Bon appetit!"
            sender_email = settings.DEFAULT_FROM_EMAIL
            send_mail(subject, message, sender_email,
                      (sender_email, customer_email), fail_silently=False,)
            messages.success(request, "An email confirmaion has been sent")
        else:
            messages.error(request, "Invalid data")
        # prevents submitting the same data twice
        return redirect('base')
    else:
        form = OrderForm()
        context = {
            "order_num": order_id,
            "order_price": order_price,
            "order_options": order_options,
            "order_toppings": order_toppings,
            "form": form
        }
        return render(request, f'pizza_app/order.html', context)


def base(request):
    return render(request, f'pizza_app/base.html')
