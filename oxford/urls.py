from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'profile/$', 'job.views.profile', name='profile'),
    url(r'map', 'job.views.map', name='map'),
    url(r'^register/$', 'job.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),

    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),



    url(r'^positions/$', 'job.views.list', name='careers_list'),
    url(r'^apply/$', 'job.views.apply', name='careers_apply'),
    url(r'^apply/thank-you/$', 'job.views.apply_done', name='careers_apply_done'),

    url(r'^api/', include('job.api.urls')),
)