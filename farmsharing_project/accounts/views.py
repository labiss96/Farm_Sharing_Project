
from django.shortcuts import render,redirect
from django.contrib import auth
from .models import *
from otherBoard.models import *
from landBoard.models import *
from accounts.models import *
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
    shared_lands_people=Land_request.objects.filter(owner=request.user.id)#내가 공유한 땅을 신청한 사람들
    shared_lands=SharingBoard.objects.filter(writer=request.user.id)#내가 공유한 땅들
    applied_lands=Land_request.objects.filter(client=request.user.id)#내가 신청한 땅들
    return render(request,'mypage.html',{'mypage_info':mypage_info, 'my_lands':my_lands, 'sharing_posts':sharing_posts, 'request_posts':request_posts,'shared_lands':shared_lands,'shared_lands_people':shared_lands_people,'applied_lands':applied_lands})
  
def land_new(request):
    region_list = Region.objects.all()
    return render(request, 'land_new.html', {"region_list":region_list})

def land_create(request):
    profile = request.user
    land = Land()
    land.region = request.POST.get('region')
    land.postcode = request.POST.get('postcode')
    land.roadAddress = request.POST.get('roadAddress')
    land.detailAddress = request.POST.get('detailAddress')
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
    land_info.postcode = request.POST.get('postcode')
    land_info.roadAddress = request.POST.get('roadAddress')
    land_info.detailAddress = request.POST.get('detailAddress')
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

def request_land(request,land_id):
    sb=SharingBoard.objects.get(id=land_id)
    owner=Profile.objects.get(username=sb.writer)
    land_request=Land_request()
    land_request.client=request.user
    land_request.owner=owner
    land_request.land=sb
    land_request.status=True
    land_request.save()
    return redirect('sb_detail',land_id)

def request_accept(request,land_id):
    tmp_land=Land_request.objects.get(id=land_id)
    tmp_land.is_completed=True
    tmp_land.save()
    sb=SharingBoard.objects.get(id=tmp_land.land.id)
    sb.is_completed=True
    sb.save()
    
    return redirect('mypage',request.user.username)

