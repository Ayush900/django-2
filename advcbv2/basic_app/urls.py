from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [

    path('school_list/',views.SchoolListView.as_view(),name = 'school_list'),
    path('<int:id>/',views.SchoolDetailView.as_view(),name = 'details'),

]
