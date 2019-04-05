from django.shortcuts import render, redirect
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment
from django.http import JsonResponse


def update_comment(request):
	notes_pk=request.session.get("notes_pk")
	
	user=request.session.get("teststudent")
	errors='评论内容不能为空'
	text = request.POST.get('text', '').strip()
	data = {}
	if text == '':
		data['status'] = 'ERROR'
		data['message'] = '评论内容不能为空'

		
	else:
		content_type = request.POST.get('content_type', '')
		object_id = int(request.POST.get('object_id', ''))
		model_class = ContentType.objects.get(model=content_type).model_class()
		model_obj = model_class.objects.get(pk=object_id)

		comment = Comment()
		comment.user = user
		comment.text = text
		comment.content_object = model_obj
		comment.save()
		#notes_pk=str(notes_pk)
		data['status'] = 'SUCCESS'
		data['user'] = comment.user
		data['comment_time'] = comment.comment_time.strftime('%Y-%m-%d %H:%M:%S')
		data['text'] = comment.text
	return JsonResponse(data)
		



	
	
   