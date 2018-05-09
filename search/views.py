from django.shortcuts import render
from django.http import HttpResponse
from search.models import Job
from django.db.models import Count
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
	context = getHomeContext()
	return TemplateResponse(request, 'index.html', context)

def user(request, name):
	context = getUserContext(name)
	print(context)
	return TemplateResponse(request, 'user.html', context)

def sn(request, sn):
	return HttpResponse("You searched for " + sn);


#First Iteration: Return username, number of prints and number of printers
def getUserContext(name):
	j = Job.objects.filter(email=name)
	numprints = len(j)
	
	sn='serial'
	all_printers = j.values(sn).order_by(sn).annotate(the_count=Count(sn))

	allPrints = getAllPrints(j);
	bestPrints = getBestPrintsBy(Job.objects.all(), name);


	dic = { 
			'username': name, 
			'numPrints': numprints, 
			'numPrinters': len(all_printers),
			'allPrints': allPrints,
			'bestPrints': bestPrints
		  }
	return dic;

def getAllPrints(jobs):
	ret = []
	labels = ['Crosslinking Duration', 'Intensity', 'Extruder pressure 1', 'Pressure 2', 'Resolution', 'Number of layers', 'Wellplate', 'Live %', 'Elasticity']
	ret.append(labels)
	for job in jobs:
		row = [job.cl_duration, job.cl_intensity, job.pressure1, job.pressure2, job.layerHeight, job.layerNum, job.wellplate, job.live, job.elasticity]
		ret.append(row);
	return ret

def getBestPrintsBy(jobs, name):
	ret = []
	labels = ['Crosslinking Duration', 'Intensity', 'Extruder pressure 1', 'Pressure 2', 'Resolution', 'Number of layers', 'Wellplate', 'Live %', 'Elasticity']
	ret.append(labels)
	bestjobs = list(jobs.filter(email=name).order_by('-live'))

	for job in bestjobs[:10]:
		row = [job.cl_duration, job.cl_intensity, job.pressure1, job.pressure2, job.layerHeight, job.layerNum, job.wellplate, job.live, job.elasticity]
		ret.append(row);
	return ret

def getHomeContext():
	username = 'email'

	n = Job.objects.values(username).order_by(username).annotate(the_count=Count(username))
	numusers = len(n)

	allJobs = Job.objects.all();

	numprints = allJobs.count()
	avgprints = numprints / numusers;

	successData = getSuccessData();

	bestPrints = getBestPrints(allJobs);

	elasticityVsLive = getElasticityVsLive(allJobs);
	return { 
			'userCount': numusers, 
			'numPrints': avgprints, 
			'successData': successData,
			'bestPrints': bestPrints,
			'elasticityData': elasticityVsLive };

def getElasticityVsLive(jobs):
	data = []
	for job in jobs:
		data.append([job.elasticity, job.live])
	print(len(data))
	return data

def getSuccessData():
	successData = []
	for i in range(0, 101):
		successData.append([i, 0])

	jobs = Job.objects.all()

	for job in jobs:
		percent = int(job.live)
		successData[percent][1] += 1
	return successData;

def getBestPrints(jobs):
	ret = []
	labels = ['User', 'Crosslinking Duration', 'Intensity', 'Extruder pressure 1', 'Pressure 2', 'Resolution', 'Number of layers', 'Wellplate', 'Live %', 'Elasticity']
	ret.append(labels)
	bestjobs = jobs.order_by('-live')[:100]

	for job in bestjobs:
		row = [job.email, job.cl_duration, job.cl_intensity, job.pressure1, job.pressure2, job.layerHeight, job.layerNum, job.wellplate, job.live, job.elasticity]
		ret.append(row);
	return ret

