# from django.contrib import admin
# from django.urls import path
# from task2.views import function_view, ClassView
# from django.http import HttpResponse


# def home_view(request):
#    return HttpResponse("<h1>Добро пожаловать на главную страницу!</h1>")


# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('function-view/', function_view, name='function_view'),
#    path('class-view/', ClassView.as_view(), name='class_view'),
#    path('', home_view, name='home'),
# ]

# from django.contrib import admin
# from django.urls import path
# from task3.views import index_view, shop_view, cart_view

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', index_view, name='index'),
#    path('shop/', shop_view, name='shop'),
#    path('cart/', cart_view, name='cart'),
# ]

# from django.contrib import admin
# from django.urls import path
# from task4.views import index_view, shop_view, cart_view

# urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', index_view, name='index'),
#    path('shop/', shop_view, name='shop'),
#    path('cart/', cart_view, name='cart'),
# ]

from django.urls import include, path
from task5.views import sign_up_by_html, sign_up_by_django

urlpatterns = [
    path("", sign_up_by_html, name="sign_up_by_html"),
    path("django_sign_up/", sign_up_by_django, name="sign_up_by_django"),
]
