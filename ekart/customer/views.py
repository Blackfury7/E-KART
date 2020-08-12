from django.shortcuts import render


from django.http import HttpResponse,JsonResponse,HttpRequest,Http404
import json
from  . models import user_basics



def login(request):
	if request.method=="POST":
		data=json.loads(request.body)
		print(data)
		user = user_basics.objects.filter(username=data['username'],password=data['password'])
		if user.exists():
			msg = {
			"type" : "success",
			"id" : user[0].id
			}
		else:msg='Invalid Details'
		msg = json.dumps(msg)
			
		return JsonResponse(msg,safe=False)



