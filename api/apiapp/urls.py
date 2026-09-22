from django.urls import path
from . import views

urlpatterns = [
    path("expenses/", views.ViewExpences.as_view()),                      
    # path("expenses/totals", views.ViewExpenseTotals.as_view()),          
    path("expenses/<int:pk>", views.ViewExpences.as_view()),         
    # path("expenses/<int:pk>/tags", views.ViewExpenseTags.as_view()),     
    # path("expenses/<int:pk>/tags/<int:tag_id>", views.ViewExpenseTagDetail.as_view()), 

    path("tags/", views.ViewTag.as_view()),     
    path("tags/<int:pk>", views.ViewTag.as_view()),                 
    path("tags/<int:pk>/expenses", views.ViewExpenseTag.as_view()),      
]