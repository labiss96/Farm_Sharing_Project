from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('questionboard_list/', views.QuestionBoardRead, name="questionboard_list"),
    path('question/detail/<int:qb_id>',views.QuestionBoardDetail, name= "qb_detail"),
    path('question/new', views.QuestionBoardNew,name="qb_new"),
    path('question/create', views.QuestionBoardCreate, name = "qb_create"),
    path('question/edit/<int:qb_id>', views.QuestionBoardEdit, name="qb_edit"),
    path('question/update/<int:qb_id>', views.QuestionBoardUpdate, name="qb_update"),
    path('question/delete/<int:qb_id>', views.QuestionBoardDelete, name="qb_delete"),
    path('question/newcomment/<int:qb_id>',views.QuestionBoardCommentNew, name="qb_commentnew"),
    path('question/deletecomment/<int:comment_id>',views.QuestionBoardCommentDelete, name="qb_commentdelete"),
    path('dealboard_list/', views.DealBoardRead, name="dealboard_list"),
    path('deal/detail/<int:db_id>', views.DealBoardDetail, name="db_detail"),
    path('deal/new', views.DealBoardNew, name="db_new"),
    path('deal/create', views.DealBoardCreate, name = "db_create"),
    path('deal/edit/<int:db_id>', views.DealBoardEdit, name = "db_edit"),
    path('deal/update/<int:db_id>', views.DealBoardUpdate, name="db_update"),
    path('deal/delete/<int:db_id>', views.DealBoardDelete, name="db_delete"),

    




]