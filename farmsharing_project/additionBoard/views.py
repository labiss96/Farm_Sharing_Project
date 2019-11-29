from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionBoard,QB_comment,DealBoard
from accounts.models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

def QuestionBoardRead(request):
    questionboards = QuestionBoard.objects.all()
    return render(request, 'questionboard_list.html', {'questionboards':questionboards})

def QuestionBoardDetail(request, qb_id):
    me = request.user.username
    comments = QB_comment.objects.filter(qbcomment = qb_id)

    qb_detail = get_object_or_404(QuestionBoard, pk = qb_id)
    return render(request,'questionboard_detail.html',{'qb':qb_detail ,'me':me, 'comments':comments})

def QuestionBoardNew(request):
    return render(request, 'questionboard_new.html')

def QuestionBoardCreate(request):
    new_qb = QuestionBoard()
    new_qb.title = request.POST['title']
    new_qb.body = request.POST['body']
    new_qb.writer = request.user
    new_qb.pub_date=timezone.datetime.now()
    new_qb.save()
    return redirect('questionboard_list')

def QuestionBoardEdit(request, qb_id):
    edit_qb = QuestionBoard.objects.get(pk=qb_id)
    return render(request, 'questionboard_edit.html',{'qb':edit_qb})

def QuestionBoardUpdate(request, qb_id):
    update_qb = QuestionBoard.objects.get(pk= qb_id)
    update_qb.title = request.POST['title']
    update_qb.body = request.POST['body']
    update_qb.writer = request.user
    update_qb.save()
    return redirect('/additionBoard/question/detail/'+str(qb_id))

def QuestionBoardDelete(request, qb_id):
    delete_qb = QuestionBoard.objects.get(pk= qb_id)
    delete_qb.delete()
    return redirect('questionboard_list')

def QuestionBoardCommentNew(request,qb_id):
    comment = QB_comment()
    user = request.user
    comment.comment_writer = get_object_or_404(Profile , username= user)
    comment.comment_content = request.POST['content']
    comment.qbcomment = get_object_or_404(QuestionBoard, pk = qb_id)
    comment.save()
    return redirect('/additionBoard/question/detail/'+str(qb_id))
    
def QuestionBoardCommentDelete(request, comment_id):
    delete_comment = QB_comment.objects.get(id=comment_id) 
    qb_id = delete_comment.qbcomment.id
    if delete_comment.comment_writer == request.user:
        delete_comment.delete()
    return redirect('/additionBoard/question/detail/'+str(qb_id))

def DealBoardRead(request):
    dealboards = DealBoard.objects.all()
    return render(request, 'dealboard_list.html', {'dealboards': dealboards})

def DealBoardDetail(request, db_id):
    me = request.user.username
    db_detail = get_object_or_404(DealBoard,pk = db_id)
    return render(request, 'dealboard_detail.html', {'db':db_detail , 'me' : me })

def DealBoardNew(request):
    return render(request, 'dealboard_new.html')

def DealBoardCreate(request):
    new_db = DealBoard()
    new_db.title= request.POST['title']
    new_db.body = request.POST['body']
    new_db.writer = request.user
    new_db.pub_date=timezone.datetime.now()
    new_db.prod_img = request.FILES.get('prod_img')
    new_db.save()
    return redirect('dealboard_list')

def DealBoardUpdate(request, db_id):
    update_db = DealBoard.objects.get(pk=db_id)
    update_db.title = request.POST['title']
    update_db.body = request.POST['body']
    update_db.writer = request.user
    update_db.prod_img = request.FILES.get('prod_img')
    update_db.save()
    return redirect('/additionBoard/deal/detail/'+ str(db_id))

def DealBoardEdit(request, db_id):
    eidt_db = DealBoard.objects.get(pk = db_id)
    return render(request,'dealboard_edit.html',{'db': eidt_db })
    
def DealBoardDelete(request, db_id):
    delete_db = DealBoard.objects.get(pk = db_id)
    delete_db.delete()
    return redirect('dealboard_list')