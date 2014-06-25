from django.shortcuts import render_to_response 
from django.views.generic.base import View 
from django.shortcuts import HttpResponseRedirect 
from django.core.urlresolvers import reverse 
from django.template import RequestContext 
from django.views.generic import ListView 

from .models import NewProjectForm, NewProject 


class NewProjectFormView(View):
    form_class = NewProjectForm

    def get(self, request):
        form = NewProjectForm()
        return render_to_response(
                'project/new.html', {'form': form},
                context_instance = RequestContext(request),)
   
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer_id = request.session['_auth_user_id']
            #instance.vcf_file = request.FILES['vcf_file']
            instance.save()
            return HttpResponseRedirect(reverse('home'))
        return render_to_response(
                'project/new.html', {'form': form},
                context_instance = RequestContext(request),)

class DashboardView(ListView):
    model = NewProject 


class ProjectDetailsView(View):
    def get(self, request, project_id):
        return render_to_response('project/details.html') 


"""
class DashboardView(View):
    def get(self, request):
        projects = NewProject.objects.all()

def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            newproject = NewProject(
                customer = request.user.id, 
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                #upload_file = request.FILES['upload_file'],
                #FTP_file = form.cleaned_data['FTP_file'],
                #tissues = form.cleaned_data['tissues'],
                #disease = form.cleaned_data['disease'],
            )
            newproject.save()

            return HttpResponseRedirect(reverse('dashboard'))
    else:
        form = NewProjectForm()

    return render_to_response(
        'project/new.html',
        {'form': form},
        context_instance = RequestContext(request)
    )



"""
