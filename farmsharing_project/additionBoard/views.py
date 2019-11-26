from django.shortcuts import render, redirect, get_object_or_404
from .models import QuestionBoard,QB_comment
from accounts.models import Profile

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