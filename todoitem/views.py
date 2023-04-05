from django.shortcuts import render,HttpResponseRedirect
from todoitem.models import Task

# Create your views here.

# to render and save task
def home(request):
    if request.method == 'POST':
        fetched_task = request.POST['task']
        task = Task(task=fetched_task)
        task.save()

        return HttpResponseRedirect('/')
    else:
        saved_tasks = Task.objects.all()
        return render(request,'todoitem/index.html',{'tasks':saved_tasks})
    

# to delete task
def delete(request,id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.delete()

    return HttpResponseRedirect('/')