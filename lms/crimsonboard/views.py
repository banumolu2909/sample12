from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import student
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
# from .forms import CustomUserCreationForm
from crimsonboard.forms import SignUpForm


# def signup1(request):
#     print("jnvdjnjd")
#     return render(request, 'signup.html')

# def signup(request):
#     # if request.user.is_authenticated:
#     #     return redirect('signin')
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             # login(request, user)
#             return redirect('/signin')
#         else:
#             return render(request, 'signup.html', {'form': form})
#     else:
#         form = CustomUserCreationForm()
#         return render(request, 'signup.html', {'form': form})

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # django.contrib.auth.login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@csrf_exempt
def Login(request):
    print("IN Login")
    # mystudents=student.objects.all().values()
    # template = loader.get_template('D:/SE/project_django/lms/crimsonboard/templates/all_students.html')
    # context = {
    #     'mystudents': mystudents,
    # }
    # return HttpResponse(template.render(context, request))
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') # user profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
    return HttpResponse('Login Page')

# def sign_up(request):
    # return HttpResponse('Sign Up Page')
    
def profile(request): 
    return render(request, 'profile.html')

def home(request): 
    return render(request, 'base.html')

def Logout(request):
    if request.user.is_authenticated:
        print('Logout User')
        logout(request)
        return render(request, 'base.html')
        