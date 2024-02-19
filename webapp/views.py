from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, CreateUserForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth      # For Logout
from django.contrib.auth import authenticate     # For Login
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "webapp/index.html")

# Register a user
def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    context = {'form': form}
    return render(request, 'webapp/register.html', context)

# Login a User
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/login.html', context)

# User Logout
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout successfully!")
    return redirect('login')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()
    context = {'records': my_records}
    return render(request, 'webapp/dashboard.html', context)


# Create a Record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)


# Update a Record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your recorded was updated!")
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context)


# Read or view singular record
@login_required(login_url='login')
def view_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'webapp/view-record.html', context)


# Delete a Record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect('dashboard')


