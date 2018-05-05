# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9+-._]+@[a-zA-Z0-9+-._]+\.[a-zA-Z]+$')


class CourseManager(models.Manager):
	def validations(self, post_data):
		errors=[]

		if len(post_data['name'])<1:
			errors.append('Name is required')
		elif len(post_data['name'])<5:
			errors.append('Name must be greater than 5 characters or more')

		if len(post_data['description'])<1:
			errors.append('Description is required')
		elif len(post_data['description'])<15:
			errors.append('Description must br greater than 5 characters or more')

		if len(errors)>0:
			return errors

		else:
			return Course.objects.create(name=post_data['name'],description=post_data['description'])




class Course(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects=CourseManager()

	def __repr__(self):
		return "<Course object: {} {}>".format(self.name, self.description)
