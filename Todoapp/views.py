from django.shortcuts import redirect, render

from Todoapp.forms import LoginForm
from .models import TodoListItem,Form
from django.http import HttpResponseRedirect 


'''def todoappView(request):
    return render(request, 'Todolist.html')'''


def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items}) 
    
def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/porapo/')

def deleteTodoView(request,i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/porapo/')
def login(request):
    form=Form.objects.all()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/porapo/')
    context={'form':form}
       
    return render(request,'form.html',context)
