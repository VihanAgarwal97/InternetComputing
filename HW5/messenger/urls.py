from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'messenger/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^inbox/$',views.inbox,name="inbox"),
    url(r'^drafts/$',views.drafts, name="drafts"),
    url(r'^sent/$',views.sent,name="sent"),
    url(r'^create/$',views.create,name="create"),
    url(r'^edit/(?P<id>[0-9]+)/$', views.create, name="edit"),
]