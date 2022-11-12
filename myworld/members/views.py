from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse   
from .models import Members

def index(request):
  myMembers = Members.objects.all().values()
  template = loader.get_template("index.html")
  context = {
    "mymembers": myMembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstName=x, lastName=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))

def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstName = first
  member.lastName = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
