from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## Introduction
    url(r'^intro/$', 'intro.views.index'),

    ## Class list
    url(r'^classlist/$', 'classlist.views.index'),

    ## Form input
    url(r'^forminput/$', 'forminput.views.index'),

    ## User Registration
    url(r'^userreg/$', 'userreg.views.index'),
    url(r'^userreg/band/(?P<band_id>\d+)/$', 'userreg.views.banddetail'),
    url(r'^userreg/band/$', 'userreg.views.bandindex'),
    url(r'^accounts/logout/$', 'userreg.views.logoutuser'),
    url(r'^accounts/login/$', 'userreg.views.loginuser'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    ## Administration
    url(r'^admin/', include(admin.site.urls)),


    ## Resource urls
    url(r'^teacher/(?P<teacher_id>\d+)/$', 'classlist.views.teacherdetail'),
    url(r'^student/(?P<student_id>\d+)/$/', 'classlist.views.studentdetail'),
    url(r'^band/(?P<band_id>\d+)/$', 'forminput.views.banddetail'),
    url(r'^band/$', 'forminput.views.bandindex'),



)
