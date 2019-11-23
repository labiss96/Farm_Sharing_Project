from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from accounts.models import Profile
# Create your views here.

#팀 모집 게시판 함수들
def join(request):
    join_home = Join.objects.all()
    return render(request, 'join.html',{'joins':join_home})

def join_detail(request, join_id):
    join_detail = get_object_or_404(Join, pk = join_id)
    scrapped=False #스크랩 여부
    if join_detail.scrap.filter(username=request.user.username).exists():
        scrapped=True
    else:
        scrapped=False
    comments = Join_comments.objects.filter(join = join_id)
    me = request.user.username
    return render(request, 'join_detail.html', {'join':join_detail,'scrapped':scrapped, 'me':me, 'comments':comments})

def join_new(request, user_id):
    myname =  Profile.objects.get(id = user_id)
    return render(request, 'join_new.html', {'myuser':myname})

def join_create(request, user_id):
    join = Join()
    join.title = request.POST['title']
    user = request.user
    join.writer = get_object_or_404(Profile, username = user)
    join.region = request.POST['region']
    join.joined_people = request.POST['joined_people']
    join.active_period = request.POST['active_period']
    join.purpose = request.POST['purpose']
    join.body = request.POST['body']
    join.save()
    return redirect('join')

def join_delete(request, delete_join_id):
    delete_join = get_object_or_404(Join, pk= delete_join_id)
    delete_join.delete()
    return redirect('join')

def join_edit(request, edit_join_id):
    edit_join = get_object_or_404(Join, pk=edit_join_id)
    return render(request, 'join_edit.html', {'join':edit_join})

def join_update(request, update_join_id):
    update_join = get_object_or_404(Join, pk=update_join_id)
    update_join.title = request.POST['title']
    update_join.region = request.POST['region']
    update_join.joined_people = request.POST['joined_people']
    update_join.active_period = request.POST['active_period']
    update_join.purpose = request.POST['purpose']
    update_join.body = request.POST['body']
    update_join.save()
    return redirect('join')

def join_scrap(request,scrap_join_id):
    scrap_join=get_object_or_404(Join,pk=scrap_join_id)
    
    if scrap_join.scrap.filter(username=request.user.username).exists():
        scrap_join.scrap.remove(request.user)
    else:
        scrap_join.scrap.add(request.user)
    scrap_join.save()

    return redirect('join_detail',scrap_join_id) 


def join_new_comment(request, join_id):
    comment = Join_comments()
    user = request.user
    comment.writer = get_object_or_404(Profile, username = user)
    comment.content = request.POST['content']
    comment.join= get_object_or_404( Join, pk= join_id)
    comment.save()
    return redirect('join_detail',join_id)

def join_delete_comment(request, comment_id):
    d_comment = Join_comments.objects.get(id=comment_id) 
    if d_comment.writer == request.user:
        d_comment.delete()

    return redirect('join_detail',d_comment.join.pk)



# 성공 사례 계시판 함수들
def review(request):
    review_home = Review.objects.all()
    return render(request, 'review.html',{'reviews':review_home})

def review_detail(request, review_id):
    review_detail = get_object_or_404(Review, pk = review_id)
    comments = Review_comments.objects.filter(review = review_id)
    me = request.user.username
    liked=False #좋아요 여부
    if review_detail.like.filter(username=request.user.username).exists():
        liked=True
    else:
        liked=False
    like_count=review_detail.total_likes()
    return render(request, 'review_detail.html', {'review':review_detail,'like_count':like_count,'liked':liked,'me':me,'comments': comments})

def review_new(request, user_id):
    myname =  Profile.objects.get(id = user_id)
    return render(request, 'review_new.html', {'myuser':myname})

def review_create(request, user_id):
    review = Review()
    review.title = request.POST['title']
    user = request.user
    review.writer = get_object_or_404(Profile, username = user)
    review.body = request.POST['body']
    review.save()
    return redirect('/otherBoard/review/'+str(review.id))

def review_delete(request, delete_review_id):
    delete_review = get_object_or_404(Review, pk= delete_review_id)
    delete_review.delete()
    return redirect('review')

def review_edit(request, edit_review_id):
    edit_review = get_object_or_404(Review, pk=edit_review_id)
    return render(request, 'review_edit.html', {'review':edit_review})

def review_update(request, update_review_id):
    update_review = get_object_or_404(Review, pk=update_review_id)
    update_review.title = request.POST['title']
    update_review.body = request.POST['body']
    update_review.save()
    return redirect('/otherBoard/review/'+str(update_review.id))
    
def review_like(request,like_review_id):
    like_review=get_object_or_404(Review,pk=like_review_id)
    if like_review.like.filter(username=request.user.username).exists():
        like_review.like.remove(request.user)
    else:
        like_review.like.add(request.user)
    return redirect('review_detail',like_review_id)   


def review_new_comment(request, review_id):
    comment = Review_comments()
    user = request.user
    comment.writer = get_object_or_404(Profile, username = user)
    comment.content = request.POST['content']
    comment.review= get_object_or_404( Review, pk= review_id)
    comment.save()
    return redirect('review_detail',review_id)

def review_delete_comment(request, comment_id):
    d_comment = Review_comments.objects.get(id=comment_id) 
    if d_comment.writer == request.user:
        d_comment.delete()

    return redirect('review_detail',d_comment.review.pk)
