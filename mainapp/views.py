from django.shortcuts import render, redirect
from items.models import Item
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login as authlogin, logout

from django.core.paginator import Paginator

# Create your views here.
def show_items(request, category=""):
	if category == "":
		items_list = Item.objects.all().order_by('-id')
	else:
		items_list = Item.objects.filter(category=category).order_by('-id')

	paginator = Paginator(items_list, 6)
	page = request.GET.get('page', 1)

	try:
		items = paginator.page(page)
	except PageNotAnInterger:
		items = paginator.page(1)
	except EmptyPage:
		items = paginator.page(paginator.num_pages)
	
	return render(request, 'mainapp/index.html', {
		'items': items
	})


	""" CREACIÓN DE USUARIOS """

def register_page(request):

	if request.user.is_authenticated:
		return redirect('index')
	else:
		register_form = RegisterForm()

		if request.method == 'POST':
			register_form = RegisterForm(request.POST)

			if register_form.is_valid():
				register_form.save()
				messages.success(request, 'Te has registrado correctamente')

				return redirect('/index')

		return render(request, 'mainapp/register.html', {
			'title':'Registro',
			'register_form': register_form
		})

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)

		if user is not None:
			authlogin(request, user)
			return redirect('index')
		else:
			messages.warning(request, 'No te has identificado')

	return render(request)

def logoutUser(request):
	logout(request)
	return redirect('index')