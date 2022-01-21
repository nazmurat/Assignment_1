from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

from .models import *

from .forms import *




def index(request):
    return render(request, 'app/index.html')


def task(request):
    tasks = Task.objects.all()
    form = TaskForm()
    
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task') 

    
    context = {'tasks':tasks , 'form':form}
    return render(request, 'app/task.html',context)


def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task')
    context = {'form':form}
    return render(request,'app/update.html' , context)


def delete(request, pk):
    item = Task.objects.get(id=pk)
    

    if request.method == "POST":
        item.delete()
        return redirect('task')

    context={'item':item}
    return render(request,'app/delete.html',context)
