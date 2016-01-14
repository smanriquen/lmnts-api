from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404
from postmanapp.models import device
from postmanapp.serializers import DeviceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class DeviceList(APIView):
	def get(self, request, format=None):
		devices = device.objects.all()
		serializer = DeviceSerializer(devices, many = True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer=DeviceSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format = None):
		pk = request.data.get('pk')
		devicex = device.objects.get(pk=pk)
		devicex.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class DeviceDetails(APIView):
	def get_object(self,pk):
		try:
			return device.objects.get(pk=pk)
		except device.DoesNotExist:
			raise Http404

	def get(self, request, pk, format = None):
		device = self.get_object(pk)
		device = DeviceSerializer(device)
		return Response(device.data)

	def put(self, request, pk, format=None):
		device =self.get_object(pk)
		serializer = DeviceSerializer(device, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		device =self.get_object(pk)
		device.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class DeviceField(APIView):
	def get_object(self,pk):
		try:
			return device.objects.get(pk=pk)
		except device.DoesNotExist:
			raise Http404

	def get(self, request, pk, field, format = None):
		device = self.get_object(pk)
		device = DeviceSerializer(device)
		return Response(device.data.get(field))





