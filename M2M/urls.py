from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^machines/$', views.MachineList.as_view()),
   # url(r'^characteristics/$', views.CharacteristicsList.as_view()),
	url(r'^machines/(?P<family>\w+)/$', views.MachineDetails.as_view(), {'machineType': '','serial': '','field':'', 'value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/$', views.MachineDetails.as_view(), {'serial':'','field':'', 'value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/(?P<serial>[0-9]{4}-[0-9]+)/$', views.MachineDetails.as_view(),  {'field':'', 'value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/(?P<serial>[0-9]{4}-[0-9]+)/characteristics/$', views.CharacteristicsDetails.as_view(), {'field':'','value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/(?P<serial>[0-9]{4}-[0-9]+)/(?P<field>\w+)/$', views.MachineDetails.as_view(), {'value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/(?P<serial>[0-9]{4}-[0-9]+)/characteristics/(?P<field>\w+)/$', views.CharacteristicsDetails.as_view(), {'value':''}),
	url(r'^machines/(?P<family>\w+)/(?P<machineType>\w+)/(?P<serial>[0-9]{4}-[0-9]+)/characteristics/(?P<field>\w+)/(?P<value>\w+)/$', views.CharacteristicsDetails.as_view()),
	
]


