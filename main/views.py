from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson
from django.contrib.auth.decorators import login_required


def welcome(request):
    return render(request, 'main/welcome.html')


@login_required(login_url="/login/")
def index(request):
    list_courses = Course.objects.all()
    return render(request, "main/home.html", {"list_courses": list_courses})


@login_required(login_url="/login/")
def course(request, pk):
    crs = get_object_or_404(Course, pk=pk)
    list_lessons = crs.lesson_set.all()
    list_courses = Course.objects.all()
    return render(request, "main/course.html", {"crs": crs,
                                                "list_lessons": list_lessons,
                                                "list_courses": list_courses,
                                                })


@login_required(login_url="/login/")
def lesson(request, pk):
    lsn = get_object_or_404(Lesson, pk=pk)
    list_courses = Course.objects.all()
    return render(request, 'main/lesson.html', {"lsn": lsn,
                                           "list_courses": list_courses,
                                           })


