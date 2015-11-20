from django.shortcuts import render
from django.http import HttpResponse
from .models import credentials
import cgi
import os
import json
from django.conf import settings
from django.template import RequestContext, loader

def index(request):
    return render(request, 'signin/index.html')

def validate(request):
    """return HttpResponse("Hello, world. You're at the polls index.")"""
    username = request.GET.get('username')
    password = request.GET.get('password')
    response = {}
    if not credentials.objects.filter(username=username):
        s = credentials(username=username, password=password)
        s.save()
        response['status'] = 'sucess'
    else:
        response['status'] = 'failure'
    json_data = json.dumps(response)
    return HttpResponse(json_data, content_type = "application/json")
def viewdetails(request):
	entries = credentials.objects.all()
	template = loader.get_template('signin/entries.html')
	context = RequestContext(request, {
		'entries': entries,
	})
	return HttpResponse(template.render(context))
