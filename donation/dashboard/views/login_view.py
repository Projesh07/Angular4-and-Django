from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from dashboard.forms.login_form import LoginForm
from django.core.urlresolvers import reverse

import requests
import json


from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)


		
		
class LoginView(View):

	template_name='login/login.html'
    
	def get(self, request, *args, **kwargs):

		if request.user.is_authenticated():
			return HttpResponseRedirect('dashboard/')
		else:	
			form =LoginForm()
			return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		
		next2=request.GET.get("next")
		form = LoginForm(request.POST or None)
		print(request.user.is_authenticated())
		print('after post')
		if form.is_valid():
            # <process form cleaned data>
			print(request.user.is_authenticated())
			username=form.cleaned_data.get("username")
			password=form.cleaned_data.get("password")
			
			print('after is valid')
			user= authenticate(username=username,password=password)
			
			login(request,user)
			if next2:
				return HttpResponseRedirect(next2)
			return HttpResponseRedirect('dashboard/')
		return render(request, self.template_name, {'form': form})

class LogoutView(View):
		def get(self,request,*args,**kwargs):
			logout(request)
			return HttpResponseRedirect(settings.LOGIN_URL) 








