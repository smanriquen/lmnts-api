from django.db import models

# Create your models here.
# class device(models.Model):
#	kind = models.CharField(max_length=140)
#	model = models.CharField(max_length=140)
#	comment = models.TextField()
#	
#	def __unicode__(self):
#		return self.kind

class device(models.Model):
	reference = models.IntegerField(primary_key=True)
	description = models.TextField(max_length=140)
	command = models.TextField()
	
	def __unicode__(self):
		return self.reference