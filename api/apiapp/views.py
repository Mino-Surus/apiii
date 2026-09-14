from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tag, Expense

class MyView(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append({
                'id': tag.id,
                'name': tag.name
            })
        obj = {
            'data': tag_list
        }
        return JsonResponse(obj)
    def get(self, request):
            expences = Expense.objects.all()
            expence_list = []
            for expence in expences:
                expence_list.append({
                    'title': expence.title,
                    'amount': expence.amount,
                    'spent_at': expence.spent_at
                })
            obj = {
                'data': expence_list
            }
            return JsonResponse(obj)

class MyView(View):
    def get(self, request):
        tag = ...
        obj = {
            'id': tag.id,
            'name': tag.name
        }
        return JsonResponse(obj)

# Реализовать модели согласно спроектированной бд
# Реализовать Get-запросы API