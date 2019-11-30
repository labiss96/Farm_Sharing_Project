from django.shortcuts import render
from otherBoard.models import Review

# Create your views here.
def home(request):
    review_home = Review.objects.all()
    review_list = []
    for review in review_home:
        review_list.append(review)
    review_list.reverse()
    for i in range(0,len(review_list)-1):
        for j in range(i,len(review_list)):
            if review_list[i].total_likes() < review_list[j].total_likes():
                review_list[i],review_list[j] = review_list[j],review_list[i]
    best_reviews = review_list[:3]
    return render(request, 'home.html',{'reviews':best_reviews})