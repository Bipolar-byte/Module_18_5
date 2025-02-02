from django.shortcuts import render


# Главная страница
def index_view(request):
    return render(request, 'third_task/index.html')


# Магазин
def shop_view(request):
    # Словарь с товарами
    products = {
        'Игровая мышь': '2 000 руб.',
        'Клавиатура': '3 500 руб.',
        'Гарнитура': '5 000 руб.',
    }
    return render(request, 'third_task/shop.html', {'products': products})


# Корзина
def cart_view(request):
    return render(request, 'third_task/cart.html')
