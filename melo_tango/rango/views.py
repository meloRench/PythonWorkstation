from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = { 'boldmessage': "viva la vida"}
	return render(request,'rango/index.html',context_dict)
   # return HttpResponse("Rango says hey there world! <br/> <a href='/rango/rc'>About</a>")

def  about(request):
	return HttpResponse("about Page!<br/> <a href='/rango/'>Index</a>")