from django.shortcuts import render

#from django.http import HttpResponse
#import datetime


def index(request):
  return render(request, 'templates/index.html')

#def current_datetime(request):
 # now = datetime.datetime.now()
 # html = "Now, it is %"% now 
 # return HttpResponse(html)

