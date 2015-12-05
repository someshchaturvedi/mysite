from django.http import HttpResponse
from django.views import generic
from .models import Blog , Author
from django.template.response import TemplateResponse

class index(generic.TemplateView):
	template_name = 'blog/index.html'
	
"""class viewblogs(generic.ListView):
	template_name = 'blog/viewblogs.html'
	context_object_name = 'latest_blog_list'
	def get_queryset(self):
		return Blog.objects.all().order_by('-pub_date')[:5]
"""
	
"""class DetailView(generic.DetailView): 
	model = Blog
	template_name = 'blog/detail.html'
"""

def DetailView(request , pk):
	a = pk
	x = Blog.objects.get(pk = a)
	return TemplateResponse(request , 'blog/detail.html' , {
	'a':x.title,
	'b':x.text,
	'c':x.pub_date
	})
		
def viewblogs(request):
	return TemplateResponse(request,'blog/viewblogs.html' ,{
		'Authorname':Author.objects.get(pk=1),
		'latest_blog_list': Blog.objects.all().order_by('-pub_date')[:5],
		})
	
class makeblog(generic.CreateView):
	model = Blog
	fields = ['title' , 'text' , 'pub_date' ]
	template_name = 'blog/makeblog.html'
	
def thanx(request):
	 return HttpResponse('thanx')