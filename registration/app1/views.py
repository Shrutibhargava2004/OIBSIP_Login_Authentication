from django.shortcuts import render, HttpResponse, redirect;
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url= 'login')
def HomePage(request):
    return render(request , 'home.html')

def SignUpPage(request):
    if request.method=='POST':
        FirstName = request.POST.get('fname')
        LastName = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        ConfirmPassword = request.POST.get('confirm-password')

        if password != ConfirmPassword:
            return HttpResponse("Passwords does not matched!!! Try again")
        else:
            my_user = User.objects.create_user(username,FirstName, password)
            my_user.save()
        # print(FullName)
            return redirect('login')
        

    return render(request , 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is inncorect!!!!!")
        
    return render (request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login') 
