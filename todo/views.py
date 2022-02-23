from django.shortcuts import render, redirect
from .models import task
from .forms import TaskForm, UpdateForm


def ListTask(request):
    queryset = task.objects.order_by('complete','due')
    form = TaskForm()
    if request.method =='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_task')
    context = {
        'tasks':queryset,
        'form':form,
        }
    return render(request, 'todo/list_task.html', context)


def UpdateTask(request, pk):
    queryset = task.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
        return redirect('list_task')

    context = {
        'form':form
        }

    return render(request, 'todo/update_task.html', context)


def deleteTask(request, pk):
	queryset = task.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('list_task')

	context = {
		'item':queryset
		}
	return render(request, 'todo/delete_task.html', context)
