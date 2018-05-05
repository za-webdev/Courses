# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Course
from django.contrib import messages

def index(request):
	data={
		'courses':Course.objects.all()
	}
	return render(request,"course_app/index.html",data)

def add(request):
	check=Course.objects.validations(request.POST)
	if type(check) is list:
		for error in check:
			messages.add_message(request,messages.ERROR,error)
	return redirect('/')

def remove(request,course_id):
	if request.method=='POST':
		Course.objects.get(id=course_id).delete()

		return redirect('/')
	else:
		return render(request, "course_app/remove.html",{"course":Course.objects.get(id=course_id)})

