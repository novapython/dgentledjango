# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from classlist.models import Teacher, Student
from forminput.models import Band
from forminput.forms import BandForm

def index(request):
    teacher_list = None
    student_list = None
    band_list = None
    user = None
    error = None
    if 'err' in request.GET and request.GET['err'] == 'invalid':
        error = 'Invalid username or password'

    if request.user.is_authenticated():
        teacher_list = Teacher.objects.all()
        student_list = Student.objects.all()
        band_list = Band.objects.all()
        user = request.user

    return render_to_response('userreg/index.html',
                                {'teacher_list': teacher_list,
                                 'student_list': student_list,
                                 'band_list': band_list,
                                 'user': user,
                                 'error': error},
                                 context_instance = RequestContext(request))

def banddetail(request, band_id):
    try:
        band = Band.objects.get(pk=band_id)
    except Band.DoesNotExist:
        raise Http404

    return render_to_response('userreg/band_detail.html',
                                {'band': band})

@login_required(login_url='/accounts/login/')
def bandindex(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/userreg/')
            else:
                print "well..."
                print request.POST
        except Exception, e:
            print e

def logoutuser(request):
    print "Logging out user"
    if request.user.is_authenticated():
        logout(request)
        return HttpResponseRedirect('/userreg/')
    else:
        print "Already logged out"
        return HttpResponseRedirect('/userreg/')

def loginuser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return HttpResponseRedirect('/userreg/?err=invalid')
    return HttpResponseRedirect('/userreg/')
