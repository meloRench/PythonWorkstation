from django.shortcuts import render
from django.http import HttpResponse

from rango.models import Category

def index(request):
	Category_list = Category.objects.order_by('-views')[:5]

	context_dict = { 'boldmessage': "viva la vida",
	                          'categories':Category_list}


	return render(request,'rango/index.html',context_dict)
   # return HttpResponse("Rango says hey there world! <br/> <a href='/rango/rc'>About</a>")

def  about(request):
	return HttpResponse("about Page!<br/> <a href='/rango/'>Index</a>")