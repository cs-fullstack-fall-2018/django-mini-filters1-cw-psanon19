from django.shortcuts import render
from filter_app1.models import ToDo


# Create your views here.
def index(request):
    todoList = ToDo.objects.order_by('due_date')
    todo_dict = {"todos": todoList}

    return render(request, 'filter_app1/index.html', todo_dict)
