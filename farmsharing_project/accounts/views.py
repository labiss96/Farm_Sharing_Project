from django.shortcuts import render,redirect
from django.contrib import auth
from .models import Profile, Land
from otherBoard.models import *
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
                    username = request.POST['username'], 
                    password = request.POST['password1'],
                    email = request.POST['email'],
                    sns_id = request.POST['sns_id'],
                    introduce = request.POST['self_introduction'],
                    profile_img = request.FILES.get('pofile_img')
                    )
                auth.login(request, user)

                return redirect('/')
        else:
            return render(request, 'signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter info
        return render(request, 'signup.html')
    return redirect('home')

def logout(request):
    auth.logout(request)
    return render(request,'login.html')
  
def mypage(request, profile_name):
    mypage_info = Profile.objects.get(username=profile_name)
    my_lands = Land.objects.filter(owner_user=mypage_info.id)
    request_posts = mypage_info.profile_rb.all()
    sharing_posts = mypage_info.profile_sb.all()
    return render(request,'mypage.html',{'mypage_info':mypage_info, 'my_lands':my_lands, 'sharing_posts':sharing_posts, 'request_posts':request_posts})
  
def land_new(request):
    return render(request, 'land_new.html')

def land_create(request):
    profile = request.user
    land = Land()
    land.region = request.POST.get('region')
    land.land_area = request.POST.get('land_area')
    land.land_condition = request.POST.get('land_condition')
    land.owner_user = request.user
    land.save()
    return redirect('../mypage/'+str(profile.username))

def land_edit(request, land_id):
    land_info = Land.objects.get(id = land_id)
    return render(request, 'land_edit.html', {'land_info':land_info})

def land_update(request, land_id):
    land_info = Land.objects.get(id = land_id)
    land_info.region = request.POST.get('region')
    land_info.land_area = request.POST.get('land_area')
    land_info.land_condition = request.POST.get('land_condition')
    land_info.owner_user = request.user
    land_info.save()
    return redirect('../mypage/'+str(request.user.username))

def land_delete(request, land_id):
    land_info = Land.objects.get(id = land_id)
    land_info.delete()
    return redirect('../mypage/'+str(request.user.username))

def Profile_update(request):
    profile=Profile.objects.get(username=request.user.username)
    profile.email=request.POST['email']
    profile.sns_id=request.POST['sns_id']
    profile.introduce=request.POST['self_introduction']
    profile.save()
    return redirect('mypage',profile.username)

def Profile_update_detail(request):
    return render(request,'Profile_update_detail.html')

def Profile_scrap(request):
    profile=Profile.objects.get(username=request.user.username)
    scrapped_profiles=profile.Profile_scrap.all()
    return render(request,'profile_scraps.html',{'scraps':scrapped_profiles})

