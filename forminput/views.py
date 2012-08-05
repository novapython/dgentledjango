# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from intro.models import Teacher, Student
from forminput.models import Band
from forminput.forms import BandForm

def index(request):
    teacher_list = Teacher.objects.all()
    student_list = Student.objects.all()
    band_list = Band.objects.all()
    return render_to_response('forminput/index.html',
                                {'teacher_list': teacher_list,
                                 'student_list': student_list,
                                 'band_list': band_list},
                                 context_instance = RequestContext(request))

def banddetail(request, band_id):
    try:
        band = Band.objects.get(pk=band_id)
    except Band.DoesNotExist:
        raise Http404

    return render_to_response('forminput/band_detail.html',
                                {'band': band})

def bandindex(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/forminput/')
            else:
                print "well..."
                print request.POST
        except Exception, e:
            print e
