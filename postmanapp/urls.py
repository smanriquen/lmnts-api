from django.conf.urls import include, url
from . import views

urlpatterns = [

	url(r'^devices/(?P<pk>[0-9]+)/(?P<field>\w+)/$', views.DeviceField.as_view()),
	url(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetails.as_view()),
    url(r'^devices/$', views.DeviceList.as_view()),
    
    
]
