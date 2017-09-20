# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from CommentManager.models import Comment
from UserManager.models import customer
from ItemManager.models import Item
from django import forms
from django.forms.models import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

# Create your views here.

@csrf_exempt
def createComment(request):
	if request.method == 'POST' and request.POST:
		try:
			phone_number = request.POST.get('phone_number', False)
			if not phone_number:
				return JsonResponse({'response': phone_number})
			try:
				user = customer.objects.get(phone_number=int(phone_number))
			except Exception as e:
				return JsonResponse({'response': str(e)})
			if not user:
				return JsonResponse({'response': 'User must be authenticated to create comment'})

			itemTitle = request.POST.get('item', False)
			item = Item.objects.get(title=itemTitle)
			if not item:
				return JsonResponse({'response': 'Comments must be associated with an item'})

			message = request.POST.get('message', False)
			if not message:
				return JsonResponse({'response': 'There needs to be a message'})

			Comment.objects.create(user=user, item=item, message=message)
			return JsonResponse({'response': 'success'})
		except Exception as e:
			return JsonResponse({'response': str(e)})
	else:
		return JsonResponse({'response': 'Not a POST method'})

def getComment(request, pk):
	if request.method == 'GET':
		id = pk
		if id:
			try:
				comment = Comment.objects.get(id=id)
				response = {
					"user": comment.user.user.username,
					"item": comment.item.title,
					"message": comment.message,
					"date_posted": comment.date_posted
				}
				return JsonResponse({'status': 'success', 'response': response})
			except ObjectDoesNotExist:
				return JsonResponse({'status': 'error', 'response': 'no object found'})
		else:
			return JsonResponse({'response': 'Comment not found'})
	else:
		return JsonResponse({'response': 'Not a GET method'})

@csrf_exempt
def updateComment(request, pk):
	if request.method == 'POST':
		id = pk
		if id:
			try:
				newMessage = request.POST.get('message', False)
				if not newMessage:
					return JsonResponse({'response': 'this is an invalid message'})
				comment = Comment.objects.get(id=id)
				comment.message = newMessage
				comment.save()
				return JsonResponse({'response': 'Comment successfully updated'})
			except:
				return JsonResponse({'response': 'Comment was not updated'})
		else:
			return JsonResponse({'response': 'Comment not found'})
	else:
		return JsonResponse({'response': 'Not a POST method'})

@csrf_exempt
def deleteComment(request, pk):
	if request.method == 'POST':
		id = pk
		if id:
			try:
				response = Comment.objects.get(id=id).delete()
				return JsonResponse({'response': 'Successfully deleted message'})
			except ObjectDoesNotExist:
				return JsonResponse({'response': 'Comment was not found'})
		else:
			return JsonResponse({'response': 'Error finding comment'})
	else:
		return JsonResponse({'response': 'Not a POST method'})


def getCommentList(request, pk):
	if request.method == 'GET':
		id = pk
		comment_list = []
		if id:
			try:
				comments = Comment.objects.all().filter(item=id)
				for comment in comments:
					c = {
						'message': comment.message,
						'user': comment.user.user.username,
						'date_posted': comment.date_posted
					}
					comment_list.append(c.copy())
				return JsonResponse({'response': comment_list})
			except Exception as e:
				return JsonResponse({'response': str(e)})
		else:
			return JsonResponse({'response': 'Error finding comments related to item id'})
	else:
		return JsonResponse({'response': 'Not a GET method'})

