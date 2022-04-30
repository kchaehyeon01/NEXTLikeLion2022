from django.shortcuts import render, redirect
from .models import ToDoList

# Create your views here.
def home(request):
    ToDoLists = ToDoList.objects.all()

    return render(request, 'home.html', { 'ToDoLists' : ToDoLists})

def new(request):
    if request.method == 'POST':
        ToDoList.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            duedate = request.POST['duedate']
        )
        return redirect('detail', ToDoList.pk)
    return render(request, 'new.html')

def detail(request, ToDoList_pk):
    post = ToDoList.objects.get(pk=ToDoList_pk)

    return render(request, 'detail.html', {'ToDoList':ToDoList})

def edit(request, ToDoList_pk):
    post = ToDoList.objects.get(pk=ToDoList_pk)

    if request.method == 'POST':
        ToDoList.objects.filter(pk=ToDoList_pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', ToDoList_pk)

    return render(request, 'edit.html', {'ToDoList':ToDoList})

def delete(request, ToDoList_pk):
    post = ToDoList.objects.get(pk=ToDoList_pk)
    post.delete()

    return redirect('home')