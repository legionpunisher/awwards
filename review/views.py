from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    '''
    function that returns the index page
    '''
    project = Project.objects.all
    return render(request,'index.html',{'content': project})

@login_required(login_url='/accounts/login/')
def profile(request,iden):
    '''
    function to return the profile of users
    '''
    profile = Profile.get_profile(identity=iden)
    project = Project.get_project(identity=iden)
    return render(request,'profile.html',{'project':project,'profile':profile})