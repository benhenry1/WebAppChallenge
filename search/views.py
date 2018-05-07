from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(input):
	return HttpResponse("You're at the Search index")
