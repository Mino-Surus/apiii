from django.forms import ModelForm
from .models import Tag, Expense, ExpenseTag

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'spent_at']

class ExpenseTagForm(ModelForm):
    class Meta:
        model = ExpenseTag
        fields = ['expense', 'tag']
