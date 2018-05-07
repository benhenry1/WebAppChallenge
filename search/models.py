from django.db import models

# Create your models here.
class Job(models.Model):
	email 		= models.CharField(max_length=50)
	serial 		= models.IntegerField(default=-1)
	live 		= models.FloatField(default=-1)
	dead 		= models.FloatField(default=-1)
	elasticity  = models.FloatField(default=0)
	pressure1 	= models.FloatField(default=-1)
	pressure2 	= models.FloatField(default=-1)
	cl_enabled 	= models.BooleanField(default=False)
	cl_duration = models.FloatField(default=-1)
	cl_intensity= models.FloatField(default=-1)
	layerNum 	= models.IntegerField(default=-1)
	layerHeight = models.FloatField(default=-1)
	wellplate 	= models.IntegerField(default=-1)

	def str(self):
		return self.title

