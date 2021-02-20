from django.shortcuts import render
from .models import Drivers

# Create your views here.
def clientsListing(request):
	# select * from Drivers
	clientsListings = Drivers.objects.all()
	print("Recived Driver Records", len(clientsListings))
	context = {'driverList' : clientsListings}
	return render(request, "clients/clients.html", context)