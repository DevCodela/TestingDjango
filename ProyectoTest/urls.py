from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal.views import EditorList, EditorDetailView, EditorCreateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
	url(r'^editores/', EditorList.as_view(), name='lista_editores'),
	url(r'^(?P<pk>\d+)/$', EditorDetailView.as_view(), name='detalle_editor'),
	url(r'^nuevo/', EditorCreateView.as_view(), name='nuevo_editor'),
)

from django.conf.urls.static import static

# for dev static files serving
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)