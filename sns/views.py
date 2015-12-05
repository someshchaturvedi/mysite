from django.shortcuts import render 
from django.http import HttpResponseRedirect , HttpResponse
from .forms import UserForm
from .models import User
from django.template.response import TemplateResponse

def index(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			x = 0
			y = User.objects.all()
			for a in y: 
				if a.name == form.cleaned_data['name'] and a.password == form.cleaned_data['password'] :
					x+=1
					break
			if x == 0:
				return HttpResponseRedirect('/sns/signup/')
			else:
				return HttpResponseRedirect('/sns/thanx/')
		
	else:
		form = UserForm()
		return render(request, 'sns/index.html', {'form': form})
		
def thanx(request):
	return HttpResponseRedirect('/blog/')

def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			a = User(name = form.cleaned_data['name'] , password = form.cleaned_data['password'])
			a.save()
			return TemplateResponse(request , 'sns/conf.html', {})
		else:
			return HttpResponse('enter a valid form!!!')
	else:
		form = UserForm()
		return render(request , 'sns/signup.html' , {'form':form})

"""def signup(request):
			return HttpResponse('signup here')"""