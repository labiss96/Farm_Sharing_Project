from django.shortcuts import render,redirect,get_object_or_404
from .models import SharingBoard
from .models import Region
from .models import RequestBoard
# from .forms import SharingBoardForm

def SharingBoardRead(request):
    sharingboards = SharingBoard.objects.all()
    return render(request, 'sharingboard_list.html', {'sharingboards': sharingboards})

def SharingBoardDetail(request,sb_id):
    sb_detail = get_object_or_404(SharingBoard,pk= sb_id)
    return render(request, 'sharingboard_detail.html', {'sb':sb_detail})

def SharingBoardNew(request):
    regionM = Region.objects.all()
    return render(request, 'sharingboard_new.html', {'regionM': regionM})

def SharingBoardCreate(request):
    new_sb = SharingBoard() 
    new_sb.title = request.POST['title']
    new_sb.region = request.POST['region']
    new_sb.land_area = request.POST['land_area']
    new_sb.sharing_term = request.POST['sharing_term']
    new_sb.is_free = request.POST['is_free']
    new_sb.amount = request.POST['amount']
    new_sb.content = request.POST['content']
    new_sb.recruitment_status = request.POST['recruitment_status']
    new_sb.land_img = request.POST['land_img']
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
    update_sb.amount = request.POST['amount']
    update_sb.content = request.POST['content']
    update_sb.recruitment_status = request.POST['recruitment_status']
    update_sb.land_img = request.POST['land_img']
    update_sb.save()
    return redirect('sharingboard')

def SharingBoardDelete(request, sb_id):
    delete_post = SharingBoard.objects.get(pk= sb_id)
    delete_post.delete()
    return redirect('sharingboard')

def RequestBoardRead(request):
    requestboards = RequestBoard.objects.all()
    return render(request, 'requestboard_list.html', {'requestboards': requestboards})

def RequestBoardDetail(request,rb_id):
    rb_detail = get_object_or_404(RequestBoard,pk= rb_id)
    return render(request, 'requestboard_detail.html', {'rb':rb_detail})

def RequestBoardNew(request):
    regionM = Region.objects.all()
    return render(request, 'requestboard_new.html', {'regionM': regionM})

def RequestBoardCreate(request):
    new_rb = RequestBoard() 
    new_rb.title = request.POST['title']
    new_rb.region = request.POST['region']
    new_rb.land_area = request.POST['land_area']
    new_rb.sharing_term = request.POST['sharing_term']
    new_rb.is_free = request.POST['is_free']
    new_rb.amount = request.POST['amount']
    new_rb.content = request.POST['content']
    new_rb.recruitment_status = request.POST['recruitment_status']
    new_rb.purpose = request.POST['purpose']
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
    update_rb.is_free = request.POST['is_free']
    update_rb.amount = request.POST['amount']
    update_rb.content = request.POST['content']
    update_rb.recruitment_status = request.POST['recruitment_status']
    update_rb.purpose = request.POST['purpose']
    update_rb.save()
    return redirect('requestboard')

def RequestBoardDelete(request, rb_id):
    delete_post = RequestBoard.objects.get(pk= rb_id)
    delete_post.delete()
    return redirect('requestboard')
    



    
