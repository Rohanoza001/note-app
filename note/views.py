from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == "POST":
        # If someone posts to this view, redirect them to register_user
        return redirect('register_user')
    return render(request, 'note/register.html')

def register_user(request):
    print("register_user view called")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        c_password = request.POST['c_password']

        if password != c_password:
            msg = "Password Do not Match"
            return render(request, 'note/register.html', {'msg': msg})

        if User.objects.filter(username=name).exists():
            msg1 = "Username already Exist"
            return render(request, 'note/register.html', {'msg1': msg1})

        if User.objects.filter(email=email).exists():
            msg2 = "Email already Exist"
            return render(request, 'note/register.html', {'msg2': msg2})

        # Correct: include username
        User_Create = User.objects.create_user(username=name, email=email, password=password)

        # Check your Register model structure
        Register.objects.create(user=User_Create, contact=contact) # ignore

        request.session['user_id'] = User_Create.id
        return redirect('homepage')

def login(request):
    return render(request, 'note/login.html')

def sign_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        
        # Try to authenticate with email as username
        user_obj = User.objects.get(email=email)
        user = authenticate(request, username=user_obj.username, password=password)
            
        if user is not None:
            auth_login(request, user)
            return redirect('homepage')
        else:
            msg4 = "Invalid Email and Password"
            return render(request, 'note/login.html', {'msg4': msg4})
    
    return render(request, 'note/login.html')

@login_required(login_url='login')
def homepage(request):
    notes = note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'note/homepage.html', {'notes': notes})

@login_required(login_url='login')
def create_note(request):
    return render(request, 'note/note.html')

@login_required(login_url='login')
def create_note_user(request):
    if request.method == "POST":
        try:
            title = request.POST['title']
            description = request.POST['description']
            user = request.user
            note.objects.create(title=title, description=description, user=user)
            return redirect('homepage')
        except Exception as e:
            # Handle any errors during note creation
            return render(request, 'note/note.html', {'error': 'Failed to create note. Please try again.'})
    return render(request, 'note/note.html')

def logout(request):
    auth_logout(request)
    return redirect('login')