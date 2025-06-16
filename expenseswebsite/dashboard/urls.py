from django.urls import path
from .views import index, expense_category_summary, income_source_summary

urlpatterns = [
    path('', index, name='dashboard'),
    path('expense_category_summary/', expense_category_summary, name='expense_category_summary'),
    path('income_source_summary/', income_source_summary, name='income_source_summary'),
]