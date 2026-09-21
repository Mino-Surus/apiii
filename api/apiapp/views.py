from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tag, Expense, ExpenseTag
from json import loads
from .forms import TagForm, ExpenseForm, ExpenseTagForm
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, 'dispatch')
class ViewTag(View):
    def get(self, request):
        tags = Tag.objects.all()
        tag_list = []
        for tag in tags:
            tag_list.append({
                'name': tag.name
            })
        obj = {
            'data': tag_list
        }
        return JsonResponse(obj)
    def post(self, request):
             raw_json = request.body
             new_data = loads(raw_json)
    
             form = TagForm(new_data)
             if form .is_valid():
                  tag = form.save()
                  return JsonResponse({'id': tag.id, 'name': tag.name})
             else:
                  return JsonResponse(
                       {'status': 'error', 'code': 400},
                       status=400
                  )
             
@method_decorator(csrf_exempt, 'dispatch')
class ViewExpences(View):
    def get(self, request):
            expenses = Expense.objects.all()
            expense_list = []
            for expense in expenses:
                expense_list.append({
                    'title': expense.title,
                    'amount': expense.amount,
                    'spent_at': expense.spent_at
                })
            obj = {
                'data': expense_list
            }
            return JsonResponse(obj)
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
        
            form = ExpenseForm(new_data)
            if form .is_valid():
                expense = form.save()
                return JsonResponse({'id': expense.id, 'name': expense.name, 'amount': expense.amount, 'spent_at': expense.spent_at, })
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                )

@method_decorator(csrf_exempt, 'dispatch')
class ViewExpenseTag(View):
    def get(self, request):
            expensetags = ExpenseTag.objects.all()
            expensetag_list = []
            for expensetag in expensetags:
                expensetag_list.append({
                    'expense': expensetag.expense,
                    'tag': expensetag.tag
                })
            obj = {
                'data': expensetag_list
            }
            return JsonResponse(obj)
    def post(self, request):
            raw_json = request.body
            new_data = loads(raw_json)
        
            form = ExpenseTagForm(new_data)
            if form .is_valid():
                expensetag = form.save()
                return JsonResponse({'expense': expensetag.expense, 'tag': expensetag.tag })
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                )

# Реализовать модели согласно спроектированной бд
# Реализовать Get-запросы API
# Реализовать Post-запросы API