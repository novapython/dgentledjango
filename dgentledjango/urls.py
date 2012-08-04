from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dgentledjango.views.home', name='home'),
    # url(r'^dgentledjango/', include('dgentledjango.foo.urls')),
    url(r'^intro/$', 'intro.views.index'),
    url(r'^teacher/(?P<teacher_id>\d+)/$', 'intro.views.teacherdetail'),
    url(r'^student/(?P<student_id>\d+)/$', 'intro.views.studentdetail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
