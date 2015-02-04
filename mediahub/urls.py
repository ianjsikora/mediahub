from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', 'media.views.add_content', name='add'),
    url(r'^movies/$', 'media.views.movies', name='movie'),
    url(r'^movies/(?P<movie_id>\w+)/$', 'media.views.view_movie', name='view_movie'),
    url(r'^series/$', 'media.views.series', name='series'),
    url(r'^series/(?P<series_id>\w+)/$', 'media.views.view_series', name='view_series'),
    url(r'^actors/$', 'media.views.actors', name='actor'),
    url(r'^directors/$', 'media.views.directors', name='director'),
    url(r'^writers/$', 'media.views.writers', name='writer'),
    url(r'^genres/$', 'media.views.genres', name='genre'),
    url(r'^genres/(?P<genre_id>\w+)/$', 'media.views.view_genre', name='view_genre'),
)