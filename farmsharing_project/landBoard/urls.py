from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('sharingboard', views.SharingBoardRead, name="sharingboard"),
    path('sharing/detail/<int:sb_id>', views.SharingBoardDetail, name="sb_detail"),
    path('sharing/new', views.SharingBoardNew, name= "sb_new"),
    path('sharing/create', views.SharingBoardCreate,name="sb_create"),
    path('sharing/edit/<int:sb_id>', views.SharingBoardEdit, name="sb_edit"),
    path('sharing/update/<int:sb_id>', views.SharingBoardUpdate, name="sb_update"),
    path('sharing/delete/<int:sb_id>', views.SharingBoardDelete, name="sb_delete"),
    path('sharing/new_comment/<int:sb_id>',views.SharingBoardCommentNew, name="SharingBoardCommentNew"),




    path('requestboard', views.RequestBoardRead, name="requestboard"),
    path('request/detail/<int:rb_id>', views.RequestBoardDetail, name="rb_detail"),
    path('request/new', views.RequestBoardNew, name= "rb_new"),
    path('request/create', views.RequestBoardCreate,name="rb_create"),
    path('request/edit/<int:rb_id>', views.RequestBoardEdit, name="rb_edit"),
    path('request/update/<int:rb_id>', views.RequestBoardUpdate, name="rb_update"),
    path('request/delete/<int:rb_id>', views.RequestBoardDelete, name="rb_delete"),
    path('request/new_comment/<int:rb_id>',views.RequestBoardCommentNew, name="RequestBoardCommentNew"),
]
