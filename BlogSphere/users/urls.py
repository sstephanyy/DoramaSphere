from django.urls import path
from .views import RegisterView, user_logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_logout, name='logout'),  # Use the custom logout view
    path('cadastro/', RegisterView.as_view(), name='cadastro')
]
