from django.db import models

class Tag(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    spent_at = models.DateField()

    def __str__(self):
        return f"{self.title} — {self.amount}"


class ExpenseTag(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
