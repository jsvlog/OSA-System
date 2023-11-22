from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('inout/', views.inout, name='inout'),
    path('inout/addToRegion/', views.addToRegion, name='addToRegion'),
    path('inout/addFromRegion/', views.addFromRegion, name='addFromRegion'),
    path('deleteTo/<int:pk>', views.deleteTo, name='deleteTo'),
    path('deleteTo/<int:pk>/confirm', views.deleteTo, name='deleteToConfirm'),
    path('updateTo/<int:pk>', views.updateTo, name='updateTo'),
    path('toDetails/<int:pk>', views.toDetails, name='toDetails'),
]