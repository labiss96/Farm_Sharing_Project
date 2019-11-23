from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

# 팀 모집 게시판
    path('join/',views.join, name = 'join'),
    path('join/<int:join_id>',views.join_detail, name = 'join_detail'),
    path('join/new/<int:user_id>',views.join_new, name = 'join_new'),
    path('join/create/<int:user_id>',views.join_create, name = 'join_create'),
    path('join/edit/<int:edit_join_id>',views.join_edit, name = 'join_edit'),
    path('join/update/<int:update_join_id>',views.join_update, name = 'join_update'),
    path('join/delete/<int:delete_join_id>',views.join_delete, name = 'join_delete'),
    path('join/scrap/<int:scrap_join_id>',views.join_scrap, name = 'join_scrap'),
    path('join/new_comment/<int:join_id>',views.join_new_comment, name = 'join_new_comment'),
    path('join/delete_comment/<int:comment_id>',views.join_delete_comment, name = 'join_delete_comment'),

#사례 게시판
    path('review/',views.review, name = 'review'),
    path('review/<int:review_id>',views.review_detail, name = 'review_detail'),
    path('review/new/<int:user_id>',views.review_new, name = 'review_new'),
    path('review/create/<int:user_id>',views.review_create, name = 'review_create'),
    path('review/edit/<int:edit_review_id>',views.review_edit, name = 'review_edit'),
    path('review/update/<int:update_review_id>',views.review_update, name = 'review_update'),
    path('review/delete/<int:delete_review_id>',views.review_delete, name = 'review_delete'),
    path('review/like/<int:like_review_id>',views.review_like, name = 'review_like'),
   

]
