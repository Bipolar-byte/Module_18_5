from django.shortcuts import render


# Главная страница
def index_view(request):
    return render(request, 'fourth_task/index.html')


# Магазин
def shop_view(request):
    # Список с играми
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    return render(request, 'fourth_task/shop.html', {'games': games})


# Корзина
def cart_view(request):
    return render(request, 'fourth_task/cart.html')
