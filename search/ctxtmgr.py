from search.models import Job
#First Iteration: Return username, number of prints and number of printers
def createUserContext(self, name):
	j = Job.objects.all()
	j.filter(email=name)
	numprints = size(j)


	dic = { 'numPrints': numprints, 'username': name, 'numPrinters': 0}
	return