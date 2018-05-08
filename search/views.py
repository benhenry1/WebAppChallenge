from django.shortcuts import render
from django.http import HttpResponse
from search.models import Job
from django.template.response import TemplateResponse


# Create your views here.
def index(request):
	return render(request, 'index.html')

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
	print(j)


	dic = { 'username': name, 'numPrints': numprints, 'numPrinters': 0}
	return dic;

