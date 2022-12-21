from django.urls import path;	#new
from django.urls import re_path;
from SampleApp1 import views;

urlpatterns = [ 
	path('one/', views.f11), 
	path('two/', views.f22),
];