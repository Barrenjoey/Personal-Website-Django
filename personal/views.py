from django.shortcuts import render

def index (request):
	return render(request, 'personal/home.html')
	
def contact(request):
	return render(request, 'personal/contact.html')
	
def accreditation(request):
	return render(request, 'personal/accred.html')