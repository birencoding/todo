from django.contrib import admin
from django.urls import path
from todo.views import HomeView
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Base views
    path('', HomeView.as_view(), name='home'),
    
]
