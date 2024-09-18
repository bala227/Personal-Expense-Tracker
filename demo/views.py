from django.shortcuts import render, get_object_or_404,redirect
from .models import Income, Expense
from django.db.models import Sum

def hello(request):
    if request.method == "POST":
        if 'name' in request.POST and 'amount' in request.POST and 'description' in request.POST:
            name = request.POST.get('name')
            amount = request.POST.get('amount')
            description = request.POST.get('description')
            Income.objects.create(name=name, amount=amount, description=description)

            return redirect('hello')

        if 'ename' in request.POST and 'eamount' in request.POST and 'edescription' in request.POST:
            ename = request.POST.get('ename')
            eamount = request.POST.get('eamount')
            edescription = request.POST.get('edescription')
            Expense.objects.create(ename=ename, eamount=eamount, edescription=edescription)
            
            return redirect('hello')
    
    
    incomes = Income.objects.all()
    expenses = Expense.objects.all()

    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0
    total_expense = expenses.aggregate(total=Sum('eamount'))['total'] or 0
    savings = total_income-total_expense

    return render(request, 'incomes/index.html', {'incomes': incomes, 'expenses': expenses,'total_income':total_income,'total_expense':total_expense,'savings':savings})

def delete_income(request, id):
    if request.method == 'POST':
        income = get_object_or_404(Income, id=id)
        income.delete()
        return redirect('hello')  

def delete_expense(request, id):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, id=id)
        expense.delete()
        return redirect('hello') 
