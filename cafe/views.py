from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer


def total_income(income):
    return round(sum(income), 3)

def minute_price(price, clock):
    minute_cost = round((price / 60) * clock, 3)
    return minute_cost

def hour_price(integer, decimal, price):
    dec = round(decimal * 100, 3)
    hour_cost = (integer * price) + (dec * (price / 60))
    return hour_cost

def home(request):
    return render(request, 'cafe/home.html')

def calculate_cost(request):
    if request.method == 'POST':
        rate_price = float(request.POST.get('rate_price'))
        vip_question = request.POST.get('vip_question')
        vip_discount_rate = float(request.POST.get('vip_discount_rate'))

        if vip_question == 'yes':
            discount_enabled = True
        else:
            discount_enabled = False

        context = {
            'rate_price': rate_price,
            'vip_discount_rate': vip_discount_rate,
            'discount_enabled': discount_enabled,
        }
        return render(request, 'cafe/calculate_cost.html', context)
    else:
        return HttpResponse('Invalid request')

def display_cost(request):
    if request.method == 'POST':
        hour = request.POST.get('hour')
        minute = request.POST.get('minute')
        rate_price = float(request.POST.get('rate_price'))
        vip_discount_rate = float(request.POST.get('vip_discount_rate'))
        discount_enabled = request.POST.get('discount_enabled') == 'True'

        if hour:
            try:
                hour = float(hour)
                integer, dec = divmod(hour, 1)
                cost = hour_price(integer, dec, rate_price)
            except ValueError:
                return HttpResponse('Invalid input for hour')
        else:
            hour = 0
            cost = 0

        if minute:
            try:
                minute = int(minute)
                cost += minute_price(rate_price, minute)
            except ValueError:
                return HttpResponse('Invalid input for minute')

        if discount_enabled:
            cost -= ((cost * vip_discount_rate) / 100)

        context = {
            'hour': hour,
            'minute': minute,
            'cost': round(cost, 3),
            'discount_enabled': discount_enabled,
        }
        return render(request, 'cafe/display_cost.html', context)
    else:
        return HttpResponse('Invalid request')
