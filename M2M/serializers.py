from M2M.models import machine
from M2M.models import characteristics
from rest_framework import serializers


class CharacteristicsSerializer(serializers.ModelSerializer):

	class Meta:
		model = characteristics
		fields = ('characteristicType', 'parent', 'value','timer', 'lastRead')


class MachineSerializer(serializers.ModelSerializer):

	characteristics = CharacteristicsSerializer(many=True, required=False)

	class Meta:
		model = machine
		fields = ('machineType', 'family', 'serial','MAC', 'services', 'characteristics')

	def create(self, validated_data):
		characteristics_data = validated_data.pop('characteristics')
		machineToCreate = machine.objects.create(**validated_data)
		for characteristics_data in characteristics_data:
		    characteristics.objects.create(parent=machineToCreate, **characteristics_data)
		return machineToCreate




		

