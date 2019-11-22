from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Profile

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = Profile.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username has already been taken'})
            except Profile.DoesNotExist:
                user = Profile.objects.create_user(
                    request.POST['username'], password=request.POST['password1'],email=request.POST['email'],sns_id=request.POST['sns_id'],
                    introduce=request.POST['self_introduction'])
                auth.login(request, user)
               

                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return redirect('home')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
  
def mypage(request):
    mypage_info=Profile.objects.get(username=request.user.username)
    return render(request,'mypage.html',{'mypage_info':mypage_info})
  
def land_new(request):
    return render(request, 'land_new.html')
