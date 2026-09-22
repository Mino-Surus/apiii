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
    def get(self, request, pk=None):                
        if pk is None:
            tags = Tag.objects.all()
            tag_list = []
            for tag in tags:
                tag_list.append({'id': tag.id, 'name': tag.name})
            return JsonResponse({'data': tag_list})
        else:
            tag = get_object_or_404(Tag, pk=pk)
            return JsonResponse({'id': tag.id, 'name': tag.name})
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
    def put(self,request,pk):
         tag = get_object_or_404(Tag, pk=pk)
         new_data = loads(request.body)
         form = TagForm(new_data, instance=tag)
         if form.is_valid():
              tag = form.save()
              return JsonResponse({'id': tag.id, 'name': tag.name})
         else:
              return JsonResponse(
                   {'status': 'error', 'code': 400, 'errors': form.errors},status=400
              )
             
@method_decorator(csrf_exempt, 'dispatch')
class ViewExpences(View):
    def get(self, request, pk=None):
            if pk is None:
                expenses = Expense.objects.all()
                expense_list = []
                for expense in expenses:
                    expense_list.append({
                        'name': expense.name,
                        'amount': expense.amount,
                        'spent_at': expense.spent_at
                    })
                obj = {
                    'data': expense_list
                }
                return JsonResponse(obj)
            else:
                expense = get_object_or_404(Expense, pk=pk)
                return JsonResponse({
                    'name': expense.name,
                    'amount': expense.amount,
                    'spent_at': expense.spent_at
                })
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
    def put(self, request, pk):
            expense = get_object_or_404(Expense, pk=pk)
            new_data = loads(request.body)
            form = ExpenseForm(new_data, instance=expense)
            if form .is_valid():
                expense = form.save()
                return JsonResponse({'id': expense.id, 'name': expense.name, 'amount': expense.amount, 'spent_at': expense.spent_at, })
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400, 'errors': form.errors},
                    status=400
                )

@method_decorator(csrf_exempt, 'dispatch')
class ViewExpenseTag(View):
    def get(self, request, pk=None):
        if pk is None:
            expensetags = ExpenseTag.objects.all()
        else:
            tag = get_object_or_404(Tag, pk=pk)
            expensetags = ExpenseTag.objects.filter(tag=tag)
        expensetag_list = []
        for et in expensetags:
            expensetag_list.append({
            'expense_id': et.expense.id,
            'expense_name': et.expense.name,
            'tag_id': et.tag.id,
            'tag_name': et.tag.name,
        })
        return JsonResponse({'data': expensetag_list})
    
    def post(self, request, pk):
            raw_json = request.body
            new_data = loads(raw_json)
            new_data['tag'] = get_object_or_404(Tag, pk=pk).pk
        
            form = ExpenseTagForm(new_data)
            if form .is_valid():
                expensetag = form.save()
                return JsonResponse({'expense': expensetag.expense.id, 'tag': expensetag.tag.id})
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400},
                    status=400
                )
    def put(self, request, pk):
            new_data = loads(request.body)
            expense_id = new_data.get('expense_id')
            expensetag = get_object_or_404(ExpenseTag, tag_id=pk, expense_id=expense_id)
            form = ExpenseTagForm(new_data, instance=expensetag)
            if form .is_valid():
                expensetag = form.save()
                return JsonResponse({'expense': expensetag.expense.id, 'tag': expensetag.tag.id})
            else:
                return JsonResponse(
                    {'status': 'error', 'code': 400, 'errors': form.errors},
                    status=400
                )

# Реализовать модели согласно спроектированной бд
# Реализовать Get-запросы API
# Реализовать Post-запросы API