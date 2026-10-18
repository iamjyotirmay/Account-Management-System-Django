from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator

class Transaction(models.Model):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"
    TYPE_CHOICES = [(INCOME, "Income"), (EXPENSE, "Expense")]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    title = models.CharField(max_length=120)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.transaction_type}: {self.title} ({self.amount})"
