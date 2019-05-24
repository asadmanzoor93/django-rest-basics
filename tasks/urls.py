from django.urls import path

from tasks import views


urlpatterns = [
    path('', views.TaskList.as_view()),
    path('<int:pk>/', views.TaskDetail.as_view()),
]
