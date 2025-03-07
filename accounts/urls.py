from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #URL links#
    path('signup/', views.sign_up, name = 'signup'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name= 'logout'),

]