from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    function that returns the index page
    '''
    project = Project.objects.all
    return render(request,'index.html',{'content': project})
