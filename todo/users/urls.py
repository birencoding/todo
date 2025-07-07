from django.urls import path
from .views import register, logout_view
from django.contrib.auth import views as auth_views
app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', register, name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('logout/',logout_view, name='logout'),
]
