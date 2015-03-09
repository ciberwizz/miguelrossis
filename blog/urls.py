from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
	url(r'^blog/$', views.PostList.as_view()),
	url(r'^blog/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
	]

urlpatterns = format_suffix_patterns(urlpatterns)
