from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/<str:profile_name>', views.mypage, name='mypage'),
    path('newLand/', views.land_new, name="land_new"),
    path('createLand/', views.land_create, name="land_create"),
    path('Profile_update/',views.Profile_update,name="Profile_update"),
    path('Profile_update_detail/',views.Profile_update_detail,name='Profile_update_detail'),
]

