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

def SchoolDetailView(request, school_id):
    pk=school_id
    school=School.objects.filter(id=pk).get()
    return render(request,'basic_app/school_details.html',{'school_details':school})

#class SchoolDetailView(DetailView,pk):
#    context_object_name = 'school_details'
#    model = School
#    template_name = 'basic_app/school_details.html'
