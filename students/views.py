from django.shortcuts import render, redirect
from .forms import RegisterForm
from main.models import Course, Lesson


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    list_courses = Course.objects.all()
    return render(request, 'students/register.html', {"form": form,
                                                      "list_courses":list_courses,

                                                      })
