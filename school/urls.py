from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('index/', views.dashboardView, name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]