from django.conf.urls import urls
from . import views

urlpatterns = [
	url(r'^blog/$', views.post_list, name = 'post_list')
]