from postmanapp.models import device
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = device
#		fields = ('kind','model','comment')

	class Meta:
		model = device
		fields = ('reference','description','command')



		

