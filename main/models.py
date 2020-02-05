from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=265, default='WRITE DESCRIPTION')
    content = models.TextField()

    def __str__(self):
        return self.name