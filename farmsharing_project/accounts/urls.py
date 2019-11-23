from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('mypage/<str:profile_name>', views.mypage, name='mypage'),
    path('Profile_update/',views.Profile_update,name="Profile_update"),
    path('Profile_update_detail/',views.Profile_update_detail,name='Profile_update_detail'),
    path('newLand/', views.land_new, name="land_new"),
    path('createLand/', views.land_create, name="land_create"),
    path('editLand/<int:land_id>', views.land_edit, name="land_edit"),
    path('updateLand/<int:land_id>', views.land_update, name="land_update"),
    path('deleteLand/<int:land_id>', views.land_delete, name="land_delete"),
    path('Profile_scrap/',views.Profile_scrap,name="Profile_scrap"),
]

