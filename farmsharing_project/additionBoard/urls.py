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



]