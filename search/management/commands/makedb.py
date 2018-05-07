import json
import os
from django.core.management.base import BaseCommand, CommandError
from search.models import Job

class Command(BaseCommand):
	def handle(self, *args, **options):
		#Only populate if necessary
		if Job.objects.all():
			print("Database is already populated.")
			return;


		#Load data from file
		alleviData = open(os.getcwd() + "/search/allevi-data.json", "r");
		data = json.load(alleviData);

		for job in data:
			#Add all jobs to db
			user = job['user_info']
			printdata = job['print_data']
			printinfo = job['print_info']

			email = user['email']
			serial = int(user['serial'])
			live = float(printdata['livePercent'])
			dead = float(printdata['deadPercent'])
			elasticity = float(printdata['elasticity'])
			pressure1 = float(printinfo['pressure']['extruder1'])
			pressure2 = float(printinfo['pressure']['extruder2'])
			clinfo = printinfo['crosslinking']
			cl_enabled = clinfo['cl_enabled'] == "True"
			cl_duration = float(clinfo['cl_duration'])
			cl_intensity = float(clinfo['cl_intensity'])
			layerNum = int(printinfo['resolution']['layerNum'])
			layerHeight = float(printinfo['resolution']['layerHeight'])
			wellplate = int(printinfo['wellplate'])

			newjob = Job(None, email, serial, live, dead, elasticity, pressure1, pressure2, cl_enabled, cl_duration, cl_intensity, layerNum, layerHeight, wellplate)
			newjob.save()

		print(Job.objects.all())

		alleviData.close()

if __name__ == "__main__":
	init();