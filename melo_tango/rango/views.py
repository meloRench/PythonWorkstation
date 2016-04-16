from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import CategoryForm

from rango.models import Category
from rango.models import Page

def index(request):
	Category_list = Category.objects.order_by('-views')[:5]

	context_dict = { 'boldmessage': "viva la vida",
	                          'categories':Category_list}


	return render(request,'rango/index.html',context_dict)
   # return HttpResponse("Rango says hey there world! <br/> <a href='/rango/rc'>About</a>")

def category(request,category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name']= category.name

		pages = Page.objects.filter(category=category)

		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render(request,'rango/category.html',context_dict)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
    	form = CategoryForm()

    return render(request, 'rango/add_category.html', {'form': form})

def  about(request):
	return HttpResponse("about Page!<br/> <a href='/rango/'>Index</a>")