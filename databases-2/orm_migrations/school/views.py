from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    context = {}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
 
    ordering = 'group'

    object_list = Student.objects.all().order_by(ordering)

    for student in object_list:
        print(f'{student.name}, {student.group}, {student.teachers}') 

    context = {'object_list': object_list}

    return render(request, template, context)
