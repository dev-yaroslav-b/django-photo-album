from django.conf.urls import url
from django.urls import include, path
from django.conf.urls.static import static

from . import views
from . import forms

from photoalbum import settings

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.DetailView.as_view(), name='details'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^post/share-video/$', views.share_video, name='share_video'),
    url(r'^post/(?P<pk>\d+)/delete_post/$',
        views.delete_post, name='delete_post'),

    url(r'^signup/$', forms.RegisterFormView.as_view()),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
