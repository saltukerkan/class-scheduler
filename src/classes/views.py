from django.shortcuts import render
from django.http import HttpResponse 
from django.views import View
# Create your views here.

def home(request):
	context = {	}
	return render(request,"home.html", context)

def about(request):
	context = { }
	return render(request,"about.html", context)

def contact(request):
	context = { }
	return render(request,"contact.html", context)

class CourseView(View):
	def get(self,request,*args,**kwargs):
		context = {
			"course_id": kwargs["id"]
		}
		return render(request,"course.html", context)