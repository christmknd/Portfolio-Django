from django.shortcuts import render
from portfolio.models import Projects

# Create your views here.

def portfolio(request):
    return render(request,'portfolio.html', {})

def projects(request):
    projects= Projects.objects.all()
    result_project = {'projects' : projects}
    return render(request, 'projects.html',result_project)

def project(request,id):
    project_id = Projects.objects.get(id=id)
    context = {'project_id': project_id }
    return render(request, 'project.html',context)