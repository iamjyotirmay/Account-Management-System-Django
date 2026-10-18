from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import RegisterForm, TransactionForm
from .models import Transaction

def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your account was created successfully.")
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})

class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = AuthenticationForm

class UserLogoutView(LogoutView):
    pass

@login_required
def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user)
    income = sum((t.amount for t in transactions if t.transaction_type == Transaction.INCOME), Decimal("0.00"))
    expenses = sum((t.amount for t in transactions if t.transaction_type == Transaction.EXPENSE), Decimal("0.00"))
    return render(request, "accounts/dashboard.html", {
        "transactions": transactions[:10],
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
    })

@login_required
def add_transaction(request):
    form = TransactionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        transaction = form.save(commit=False)
        transaction.user = request.user
        transaction.save()
        messages.success(request, "Transaction added.")
        return redirect("dashboard")
    return render(request, "accounts/transaction_form.html", {"form": form})

@login_required
@require_POST
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    transaction.delete()
    messages.success(request, "Transaction deleted.")
    return redirect("dashboard")
