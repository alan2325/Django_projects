# from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.fun1),
    path('fun2',views.fun2),
    path('fun3/<int:a>/<b>',views.fun3),
    path('fun4/<int:a>/<int:b>',views.fun4),
    path('emp/<int:year>/<int:sal>',views.emp),
    path('bill/<int:unit>',views.bill),
    path('day/<int:day>',views.day),
    path('city/<city>',views.city)
]