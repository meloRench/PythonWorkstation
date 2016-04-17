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

from rango.forms import UserForm, UserProfileForm

def register(request):

    registered = False

    if request.method == 'POST':
       
       
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

       
        if user_form.is_valid() and profile_form.is_valid():
       
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
       
        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def  about(request):
	return HttpResponse("about Page!<br/> <a href='/rango/'>Index</a>")