# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader
from classlist.models import Teacher, Student

def index(request):
    teacher_list = Teacher.objects.all()
    student_list = Student.objects.all()
    return render_to_response('classlist/index.html',
                                {'teacher_list': teacher_list,
                                 'student_list': student_list})

def teacherdetail(request, teacher_id):
    try:
        teacher = Teacher.objects.get(pk=teacher_id)
    except Teacher.DoesNotExist:
        raise Http404

    return render_to_response('classlist/teacher_detail.html',
                                {'teacher': teacher})

def studentdetail(request, student_id):
    try:
        student = Student.objects.get(pk=student)
    except Student.DoesNotExist:
        raise Http404

    return render_to_response('classlist/student_detail.html',
                                {'student': student})
