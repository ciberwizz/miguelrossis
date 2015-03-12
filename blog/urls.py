from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
	url(r'^api/blog/$', views.PostList.as_view()),
	url(r'^api/blog/(?P<pk>[0-9]+)/$', views.PostDetail.as_view()),
	url(r'^$', views.posts),
	]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = format_suffix_patterns(urlpatterns)
