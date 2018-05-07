from django.shortcuts import render
from django.http import HttpResponse
import ctxtmgr

# Create your views here.
def index(request):
	return render(request, 'index.html')

def user(request, name):

	return HttpResponse("You searched for " + name);

def sn(request, sn):
	return HttpResponse("You searched for " + sn);
