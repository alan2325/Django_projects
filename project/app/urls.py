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
    path('city/<city>',views.city),
    path('tax/<int:costprice>',views.tax),
    path('div/<int:num>',views.div),
    path('html',views.html),
    path('html2',views.html2),
    path('std',views.std),
    path('above',views.above),
    path('below',views.below),
    path('view',views.view),
    path('form',views.form),
    path('edit/<std>',views.edit),
    path('delete/<nm>',views.delete)
]