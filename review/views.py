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
@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.by = current_user
            project.save()
        return redirect('home')

    else:
        form= NewProjectForm()

    return render(request, 'new_project.html', {'form':form})
@login_required(login_url='/accounts/login/')
def search(request):
    if 'project' in request.GET and request.GET['project']:
        name = request.GET.get('project')
        project = Project.search(name)

        return render(request, 'search.html', {'title':name, 'content':project})

    else:
        return render(request,'search.html')