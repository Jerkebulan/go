from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name="index"),
    path('course/<int:pk>', views.course, name="course"),
    path('lesson/<int:pk>', views.lesson, name="lesson"),
    path('', views.welcome, name="welcome"),
]