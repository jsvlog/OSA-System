from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('inout/', views.inout, name='inout'),
    path('inout/addToRegion/', views.addToRegion, name='addToRegion'),
    path('inout/addFromRegion/', views.addFromRegion, name='addFromRegion'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),

]