from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import Http404
from M2M.models import machine
from M2M.models import characteristics
from M2M.serializers import MachineSerializer
from M2M.serializers import CharacteristicsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MachineList(APIView):
	def get(self, request, format=None):
		machines = machine.objects.all()
		serializedMachines = MachineSerializer(machines, many = True)
		return Response(serializedMachines.data)

	def post(self, request, format=None):
		serializedMachines=MachineSerializer(data=request.data)
		if serializedMachines.is_valid():
			serializedMachines.save()
			return Response(serializedMachines.data, status = status.HTTP_201_CREATED)
		return Response(serializedMachines.errors, status = status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format = None):
		serial = request.data.get('serial')
		machineToDelete = machine.objects.get(serial=serial)
		machineToDelete.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class MachineDetails(APIView):

	def get(self, request, family, machineType, serial, field, value, format = None):
		
		if field:
			machine = getJustOneMachine(family, machineType, serial)
			serializedMachine = MachineSerializer(machine)
			return Response(serializedMachine.data.get(field))
		else:
			machine = getMachine(family, machineType, serial)
			machines = MachineSerializer(machine, many=True)
			return Response(machines.data)

	def put(self, request, family, machineType, serial, field, value, format=None):
		
		machine = getJustOneMachine(family, machineType, serial)
		serializedMachine = MachineSerializer(machine, data=request.data)
		if serializedMachine.is_valid():
			serializedMachine.save()
			return Response(serializedMachine.data)
		return Response(serializedMachine.errors, status=status.HTTP_400_BAD_REQUEST)
				

	def delete(self, request, family, machineType, serial, field, value, format=None):
		
		machine = getMachine(family, machineType, serial)
		machine.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		

class CharacteristicsDetails(APIView):

	def get(self, request, family, machineType, serial, field, value, format = None):
		
		machine = getJustOneMachine(family, machineType, serial)
		 
		if not field:
			characteristics = machine.characteristics.all()
			serializedCharacteristics = CharacteristicsSerializer(characteristics, many=True)
			return Response(serializedCharacteristics.data)
		else:	 
			characteristics = machine.characteristics.get(characteristicType__iexact=field)
			serializedCharacteristics = CharacteristicsSerializer(characteristics)
			if value:
				return Response(serializedCharacteristics.data.get(value))
			else:
				return Response(serializedCharacteristics.data)

	def post(self, request, family, machineType, serial, field, value, format=None):

		machine = getJustOneMachine(family, machineType, serial)
		request.data['parent'] = machine.serial
		serializedCharacteristics=CharacteristicsSerializer(data=request.data)
		if serializedCharacteristics.is_valid():
			serializedCharacteristics.save()
			return Response(serializedCharacteristics.data, status = status.HTTP_201_CREATED)
		return Response(serializedCharacteristics.errors, status = status.HTTP_400_BAD_REQUEST)
		
	def put(self, request, family, machineType, serial, field, value, format=None):

		machine = getJustOneMachine(family, machineType, serial)
		characteristics = machine.characteristics.get(characteristicType__iexact=field)
		if not value:		
			serializedCharacteristics = CharacteristicsSerializer(characteristics, data=request.data)
			if serializedCharacteristics.is_valid():
				serializedCharacteristics.save()		
		else:
			characteristics.value = request.data.get(value)
			characteristics.save()
			serializedCharacteristics = CharacteristicsSerializer(characteristics)
		return Response(serializedCharacteristics.data)
		return Response(serializedCharacteristics.errors, status=status.HTTP_400_BAD_REQUEST)
		
	def delete(self, request,  family, machineType, serial, field, value, format=None):
			
		machine = getJustOneMachine(family, machineType, serial)
		if not field:
			characteristics = machine.characteristics.all()
		else:
			characteristics = machine.characteristics.get(characteristicType__iexact=field)
		characteristics.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	

#--------------- Extra functions!

def getMachine(family, machineType, serial):

		try:
			foundMachine = machine.objects.all()
			if family:
				foundMachine = foundMachine.filter(family__iexact=family)
			if machineType:
				foundMachine = foundMachine.filter(machineType__iexact=machineType)
			if serial:
				foundMachine = foundMachine.filter(serial__exact=serial)
			return foundMachine
		except machine.DoesNotExist:
			raise Http404

def getJustOneMachine(family, machineType, serial):
		machine = getMachine(family, machineType, serial)
		return machine[:1].get()






