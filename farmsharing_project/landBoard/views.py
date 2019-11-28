from django.shortcuts import render,redirect,get_object_or_404
from .models import SharingBoard
from .models import Region
from .models import RequestBoard
from accounts.models import *
from .models import SB_comment,RB_comment
from django.core.exceptions import ObjectDoesNotExist
# from .forms import SharingBoardForm
from django.core.paginator import Paginator

def SharingBoardRead(request):
    sharingboards = SharingBoard.objects.all()
    paginator = Paginator(sharingboards,2)

    page = request.GET.get('page')
    sharingboards2 = paginator.get_page(page)
    region_list = Region.objects.all()
    return render(request, 'sharingboard_list.html', {'sharingboards': sharingboards, 'region_list':region_list, 'sharingboards2':sharingboards2})

# filter
def sharing_filter(request):
    region_list = Region.objects.all()
    filter_region = request.POST.get('region')
    filter_is_free = request.POST.get('is_free')

    if(filter_region == "All" and filter_is_free == "All"):
        sharingboards = SharingBoard.objects.all()
    elif(filter_region == "All" and filter_is_free != "All"):
        sharingboards = SharingBoard.objects.filter(
            is_free = filter_is_free
        )
    elif(filter_region != "All" and filter_is_free == "All"):
        sharingboards = SharingBoard.objects.filter(
            region = filter_region
        )
    elif(filter_region != "All" and filter_is_free != "All"):
        sharingboards = SharingBoard.objects.filter(
            region = filter_region,
            is_free = filter_is_free
        )

    return render(request, 'sharingboard_list.html', {'sharingboards': sharingboards, 'region_list':region_list})


def SharingBoardNew(request):
    regionM = Region.objects.all()
    user = request.user
    user_lands = user.user_land.all()
    return render(request, 'sharingboard_new.html', {'regionM': regionM, 'user_lands':user_lands})

def SharingBoardCreate(request):

    land_id = request.POST['choice_land']
    land = Land.objects.get(id = land_id)

    new_sb = SharingBoard() 
    new_sb.title = request.POST['title']
    new_sb.region = land.region
    new_sb.land_area = request.POST['land_area']
    new_sb.sharing_term = request.POST['sharing_term']
    new_sb.is_free = request.POST['is_free']
    new_sb.amount = request.POST['amount']
    new_sb.content = request.POST['content']
    new_sb.land_img = request.FILES.get('land_img')
    new_sb.writer = request.user
    new_sb.choice_land = land

    new_sb.save()
    return redirect('sharingboard')

def SharingBoardEdit(request,sb_id):
    regionM = Region.objects.all()
    edit_sb = SharingBoard.objects.get(pk=sb_id)
    return render(request,'sharingboard_edit.html',{'sb':edit_sb , 'regionM': regionM})

def SharingBoardUpdate(request,sb_id):
    update_sb = SharingBoard.objects.get(pk=sb_id) 
    update_sb.title = request.POST['title']
    update_sb.region = request.POST['region']
    update_sb.land_area = request.POST['land_area']
    update_sb.sharing_term = request.POST['sharing_term']
    update_sb.is_free = request.POST['is_free']

    if(request.POST.get('is_free') == False):
        update_sb.amount = request.POST['amount']
    else:
        update_sb.amount = 0

    update_sb.content = request.POST['content']
    update_sb.land_img = request.POST['land_img']
    update_sb.save()
    return redirect('sharingboard')

def SharingBoardDelete(request, sb_id):
    delete_post = SharingBoard.objects.get(pk= sb_id)
    delete_post.delete()
    return redirect('sharingboard')

def RequestBoardRead(request):
    requestboards = RequestBoard.objects.all()
    region_list = Region.objects.all()
    return render(request, 'requestboard_list.html', {'requestboards': requestboards, 'region_list':region_list})

    # filter
def request_filter(request):
    region_list = Region.objects.all()
    filter_region = request.POST.get('region')
    filter_is_free = request.POST.get('is_free')

    if(filter_region == "All" and filter_is_free == "All"):
        requestboards = RequestBoard.objects.all()
    elif(filter_region == "All" and filter_is_free != "All"):
        requestboards = RequestBoard.objects.filter(
            is_free = filter_is_free
        )
    elif(filter_region != "All" and filter_is_free == "All"):
        requestboards = RequestBoard.objects.filter(
            region = filter_region
        )
    elif(filter_region != "All" and filter_is_free != "All"):
        requestboards = RequestBoard.objects.filter(
            region = filter_region,
            is_free = filter_is_free
        )

    return render(request, 'requestboard_list.html', {'requestboards': requestboards, 'region_list':region_list})


def SharingBoardDetail(request,sb_id):
    sb_detail = get_object_or_404(SharingBoard,pk= sb_id)
    comments = SB_comment.objects.filter(sbcomment = sb_id)
    me = request.user.username
    sb=SharingBoard.objects.get(id=sb_id)
    requested=False
    if sb.writer.username != request.user.username:
        try:
            land=Land_request.objects.get(land=sb.choice_land.id, client=request.user.id)
            requested=land.status
        except ObjectDoesNotExist:
            pass
    

    return render(request, 'sharingboard_detail.html', {'sb':sb_detail, 'me':me, 'comments':comments,'requested':requested})

def RequestBoardDetail(request,rb_id):
    rb_detail = get_object_or_404(RequestBoard,pk= rb_id)
    comments = RB_comment.objects.filter(rbcomment = rb_id)
    me = request.user.username
    land = request.user.user_land.all()
    return render(request, 'requestboard_detail.html', {'rb':rb_detail, 'land':land, 'me':me,'comments':comments})

def RequestBoardNew(request):
    regionM = Region.objects.all()
    return render(request, 'requestboard_new.html', {'regionM': regionM})

def RequestBoardCreate(request):
    new_rb = RequestBoard() 
    new_rb.title = request.POST['title']
    new_rb.region = request.POST['region']
    new_rb.land_area = request.POST['land_area']
    new_rb.sharing_term = request.POST['sharing_term']
    new_rb.is_pay_for = request.POST['is_pay_for']
    new_rb.content = request.POST['content']
    new_rb.purpose = request.POST['purpose']
    new_rb.writer = request.user
    new_rb.save()
    return redirect('requestboard')

def RequestBoardEdit(request,rb_id):
    regionM = Region.objects.all()
    edit_rb = RequestBoard.objects.get(pk=rb_id)
    return render(request,'requestboard_edit.html',{'rb':edit_rb , 'regionM': regionM})

def RequestBoardUpdate(request,rb_id):
    update_rb = RequestBoard.objects.get(pk=rb_id) 
    update_rb.title = request.POST['title']
    update_rb.region = request.POST['region']
    update_rb.land_area = request.POST['land_area']
    update_rb.sharing_term = request.POST['sharing_term']
    update_rb.is_pay_for = request.POST['is_pay_for']
    update_rb.content = request.POST['content']
    update_rb.purpose = request.POST['purpose']
    update_rb.save()
    return redirect('requestboard')

def RequestBoardDelete(request, rb_id):
    delete_post = RequestBoard.objects.get(pk= rb_id)
    delete_post.delete()
    return redirect('requestboard')


def SharingBoardCommentNew(request,sb_id):
    comment = SB_comment()
    user = request.user
    comment.comment_writer = get_object_or_404(Profile , username= user)
    comment.comment_content = request.POST['content']
    comment.sbcomment = get_object_or_404(SharingBoard, pk = sb_id)
    comment.save()
    return redirect('sb_detail',sb_id)

def RequestBoardCommentNew(request,rb_id):
    comment = RB_comment()
    user = request.user
    comment.comment_writer = get_object_or_404(Profile, username=user)
    land_id = request.POST['l']
    land = Land.objects.get(id = land_id)
    comment.land_writer = land
    comment.comment_content = request.POST['content']
    comment.rbcomment = get_object_or_404(RequestBoard, pk=rb_id)
    comment.save()
    return redirect('rb_detail',rb_id)



