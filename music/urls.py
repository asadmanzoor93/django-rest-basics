from django.urls import path
from music import views


urlpatterns = [
    path('songs/', views.ListSongsView.as_view(), name="songs-all"),
    path('auth/login/', views.LoginView.as_view(), name="auth-login"),
    path('auth/register/', views.RegisterUsers.as_view(), name="auth-register")

]
