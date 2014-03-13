from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from shiva import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'faces.views.home', name='home'),

    url(r'^api/get_faces/$', 'faces.api.get_faces', name='get_faces'),
    url(r'^api/is_solved/$', 'faces.api.is_solved', name='is_solved'),
    url(r'^api/get_faces/(?P<selected_pk>\d+)$', 'faces.api.get_faces', name='get_faces'),
    url(r'^api/get_guesses/(?P<face_pk>\d+)$', 'faces.api.guess', name='get_guesses'),
    url(r'^api/put_guess/(?P<face_pk>\d+)$', 'faces.api.guess', name='put_guess'),
    url(r'^api/get_chat/$', 'faces.api.chat', name='get_chat'),
    url(r'^api/put_msg/$', 'faces.api.chat', name='put_chat'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
