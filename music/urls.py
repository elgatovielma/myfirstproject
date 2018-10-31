
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views


app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$',login_required(views.IndexView.as_view()),name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),

    # /music/album/add
    url(r'album/add/$',views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<album_id>
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<album_id>/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name='album-delete'),

    # music/logout
    url(r'logout/$',views.LogoutView.as_view(), name="logout"),

    # music/login/
    url(r'login/$', views.LoginView.as_view(), name="login"),
]
