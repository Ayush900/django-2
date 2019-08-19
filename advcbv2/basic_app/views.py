from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from basic_app.models import School,Student

# Create your views here.

class IndexPageView(TemplateView):

    template_name = 'basic_app/index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTED TEXT!!'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School

class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = School
    template_name = 'basic_app/school_details.html'
