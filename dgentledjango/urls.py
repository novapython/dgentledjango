from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ## Introduction
    url(r'^intro/$', 'intro.views.index'),
    url(r'^teacher/(?P<teacher_id>\d+)/$', 'intro.views.teacherdetail'),
    url(r'^student/(?P<student_id>\d+)/$', 'intro.views.studentdetail'),

    ## Form input
    url(r'^forminput/$', 'forminput.views.index'),
    url(r'^band/(?P<band_id>\d+)/$', 'forminput.views.banddetail'),
    url(r'^band/$', 'forminput.views.bandindex'),


    ## User Registration
    url(r'^accounts/', include('registration.backends.default.urls')),

    ## Administration
    url(r'^admin/', include(admin.site.urls)),
)
