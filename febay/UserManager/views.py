# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, customer
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):
	if request.method == 'POST':
		user = customer.objects.create_user(
			first_name = request.POST.get('first_name'),
			last_name = request.POST.get('last_name'),
			username = request.POST.get('username'),
			email = request.POST.get('email'),
			city = request.POST.get('city'),
			state = request.POST.get('state'),
			phone_number = request.POST.get('phone_number'),
			password = request.POST.get('password')
			)
		return JsonResponse({'Response':{'first name': user.first_name,'last name': user.last_name, 'username': user.username, 'email': user.email, 'state':user.state, 'city':user.city, 'phone number': user.phone_number,'id':user.id}})
	else:
		return JsonResponse({'Response': 'Could not register user'})

@csrf_exempt
def get_user(request,id):
	response = {}
	if request.method == 'GET':
		try:
			user = customer.objects.get(id = id)
			print(user)
			response[user.username] = {'first name': user.first_name,'last name': user.last_name, 
			'username': user.username, 'email': user.email, 'state':user.state, 
			'city':user.city, 'phone number': user.phone_number,'id':user.id}
		except():
			pass
	return JsonResponse(response)

# @csrf_exempt
# def get_users(request):
#     users = customer.objects.all().values('username','first_name', 'last_name')  # or simply .values() to get all fields
#     users_list = list(users)  # important: convert the QuerySet to a list object
#     return JsonResponse(users_list, safe=False)

# def login_view(request):
#     if request.method == 'POST':
#         login_form = LoginForm(data=request.POST)
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 print("You have a disabled account")
#         else:
#             print("You were not found")
#     else:
#         login_form = LoginForm()
#     return render(request , 'login.html', {'login_form': login_form})


# def logout_view(request):
#     login_form = LoginForm()
#     print(request.user)
#     logout(request)
#     print(request.user)
#     return HttpResponseRedirect('/login')