from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index.as_view(), name='index'), 
	url(r'^viewblogs/$', views.viewblogs, name= 'viewblogs') ,
	url(r'^viewblogs/(?P<pk>[0-9]+)/$', views.DetailView, name = 'detail'),
	url(r'^makeblog/$', views.makeblog.as_view() , name= 'makeblog') ,
	url(r'^thanx/$', views.thanx , name= 'thanx')
]