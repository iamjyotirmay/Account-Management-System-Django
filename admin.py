from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "transaction_type", "amount", "date")
    list_filter = ("transaction_type", "date")
    search_fields = ("title", "user__username")
