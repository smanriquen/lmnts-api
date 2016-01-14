from django.db import models

# Create your models here.

class machine(models.Model):
	machineType = models.CharField(max_length=140, blank=True)
	family = models.CharField(max_length=140, blank=True)
	serial = models.CharField(max_length=100, primary_key=True, blank=True)
	MAC = models.CharField(max_length=20, blank=True)
	services = models.TextField(null=True, blank=True)

	

class characteristics(models.Model):
	characteristicType = models.CharField(max_length=140, blank=True)
	parent = models.ForeignKey(machine, related_name='characteristics', on_delete=models.CASCADE, blank=True)
	value = models.CharField(max_length=140, blank=True)
	timer = models.CharField(max_length=140, blank=True)
	lastRead = models.DateTimeField(auto_now=True, blank=True)
	
	def __unicode__(self):
		return '%s: %s' % (self.characteristicType, self.value)



