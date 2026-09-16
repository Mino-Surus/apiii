from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Tag, Expense
from json import loads
from .forms import TagForm
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
                  return self.get(request, tag.pk)
             else:
                  return JsonResponse(
                       {'status': 'error', 'code': 400},
                       status=400
                  )
             
@method_decorator(csrf_exempt, 'dispatch')
class ViewExpences(View):
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

# Реализовать модели согласно спроектированной бд
# Реализовать Get-запросы API
# Реализовать Post-запросы API