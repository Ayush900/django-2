from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [

    path('school_list/',views.SchoolListView.as_view(),name = 'school_list'),
    path('school_list/<int:school_id>/',views.SchoolDetailView,name = 'details'),

]
