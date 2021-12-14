from django.shortcuts import redirect, render
from .models import todoItem
from django.contrib.auth.decorators import login_required
from .forms import todoforms





@login_required(login_url='/account/login')
def todo_list_view (request):
    user = request.user
    query = todoItem.objects.filter(owner=user)

    if request.method == 'POST':
       check_list= request.POST.getlist('check')
       check_list=[int(i) for i in check_list]
       for todo_item in query:
            if todo_item.id in check_list:
                todoItem.objects.filter(id=todo_item.id).update(check=True)
            else:
                todoItem.objects.filter(id= todo_item.id).update (check=False)
       return redirect('/')

    todo_len=len(query)
    return render (request,'todoapp/todo_list.html',{'todoItem':query,'todolen':todo_len})

@login_required(login_url='/account/login')
def todo_create_item (request):
    user=request.user
    if request.method == 'POST':
        form= todoforms(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner= user
            instance.save()
            return redirect('todoapp:todo_list')
    form = todoforms()
    return render (request,'todoapp/todo_create.html',{'form':form})

def todo_remove (request,id):
    try:
        item=todoItem.objects.get(id=id)
    except:
        pass

    if item.owner == request.user :
        item.delete()
        return redirect('/list')
    else:
        return redirect('/list')
    

    