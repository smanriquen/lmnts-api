from M2M.models import machine
from M2M.models import characteristics
from rest_framework import serializers


class CharacteristicsSerializer(serializers.ModelSerializer):

	class Meta:
		model = characteristics
		fields = ('characteristicType', 'parent', 'value','timer', 'lastRead')


class MachineSerializer(serializers.ModelSerializer):

	characteristics = serializers.StringRelatedField(many=True, required=False)

	class Meta:
		model = machine
		fields = ('machineType', 'family', 'serial','MAC', 'services', 'characteristics')




		

