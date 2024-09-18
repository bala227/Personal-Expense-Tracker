from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello,name='hello'),
    path('delete_income/<int:id>/', views.delete_income, name='delete_income'),
    path('delete_expense/<int:id>/', views.delete_expense, name='delete_expense')
]
