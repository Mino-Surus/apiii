from django.contrib import admin
from .models import Tag, Expense, ExpenseTag

admin.site.register(Tag)
admin.site.register(Expense)
admin.site.register(ExpenseTag)



