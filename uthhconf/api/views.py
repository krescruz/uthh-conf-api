from django.http.response import HttpResponse

def home(request):
	return HttpResponse('Home Rest Api')
