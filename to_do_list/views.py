from django.http import HttpResponse
from django.shortcuts import render

from to_do_list.models import ToDo

def create_todo(request):
    todo = ToDo(name=request.POST['name'])
    todo.save()

    return HttpResponse('', status=201)



# Create your views here.
