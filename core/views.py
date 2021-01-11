from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import *
def Index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        user = authenticate(request,email=email,password=password)
        if user is None:
            print('hsh')
            return render(request,'index.html')
        else:
            login(request,user)
            if user.role == 'admin':
                return redirect('admin')
            else:
                return redirect('user')
    return render(request,'index.html')

@login_required(login_url='')
def AdminUser(request):
    if request.user.role == 'admin':
        todo = Todo.objects.all()
        print(todo)
        context = {
            "todo":todo
        }
        return render(request,'adminhome.html',context)
    else:
        return redirect('index')

@login_required(login_url='')
def Users(request):
    todo = Todo.objects.all()
    print(todo)
    context = {
        "todo":todo
    }
    return render(request,'userhome.html',context)

@login_required(login_url='')
def NewTask(request):
    if request.user.role == 'admin':
        form = TodoForms()
        if request.method == 'POST':
            form = TodoForms(request.POST)
            if form.is_valid():
                print('demo')
                form.save()
            return redirect('admin')
        context = {
            'form':form
        }
        return render(request,'newtask.html',context)
    return redirect('index')
