import datetime
from django.http import JsonResponse
from django.shortcuts import render
from expenses.models import Expense
from userincome.models import UserIncome
from django.contrib.auth.decorators import login_required

@login_required(login_url='/authentication/login')

def index(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30*6)

    expenses = Expense.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    incomes = UserIncome.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)

    total_expenses = sum(expense.amount for expense in expenses)
    total_incomes = sum(income.amount for income in incomes)
    budget = total_incomes - total_expenses

    context = {
        'total_expenses': total_expenses,
        'total_incomes': total_incomes,
        'budget': budget,
    }

    return render(request, 'dashboard/index.html', context)

@login_required(login_url='/authentication/login')

def expense_category_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30*6)
    expenses = Expense.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(expense):
        return expense.category
    category_list = list(set(map(get_category, expenses)))

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)
        for item in filtered_by_category:
            amount += item.amount
        return amount
    
    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)

    return JsonResponse({'expense_category_data': finalrep}, safe=False) 

@login_required(login_url='/authentication/login')

def income_source_summary(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30*6)
    incomes = UserIncome.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_source(income):
        return income.source
    source_list = list(set(map(get_source, incomes)))

    def get_income_source_amount(source):
        amount = 0
        filtered_by_source = incomes.filter(source=source)
        for item in filtered_by_source:
            amount += item.amount
        return amount
    
    for x in incomes:
        for y in source_list:
            finalrep[y] = get_income_source_amount(y)

    return JsonResponse({'income_source_data': finalrep}, safe=False) 

