from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    #path('', views.student_cabinet, name="student_cabinet"),
]