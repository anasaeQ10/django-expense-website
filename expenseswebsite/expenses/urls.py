from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt,csrf_protect

urlpatterns = [   
    path('',views.index, name="expenses"),
    path('add-expenses',views.add_expenses, name="add-expenses"),
    path('edit-expense/<int:id>',views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>',views.delete_expense, name="expense-delete"),
    path('search-expenses',csrf_exempt(views.search_expenses), name="search_expenses"),
    path('expense_category_summary',views.expense_category_summary, name='expense_category_summary'),
    path('stats',views.stats_view, name='stats'),
    path('export_csv',views.export_csv, name='export-csv'),
    path('export_excel',views.export_excel, name='export-excel'),
]
