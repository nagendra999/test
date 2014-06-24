from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required 

from .views import NewProjectFormView, DashboardView


urlpatterns = patterns('',
        url(r'^new/$', login_required(NewProjectFormView.as_view()), name='project_new'),
        url(r'^dashboard/$', DashboardView.as_view(), name='dash'),
)