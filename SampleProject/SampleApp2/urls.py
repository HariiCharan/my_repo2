from django.urls import path;	#new
from django.urls import re_path;
from SampleApp2 import views;

urlpatterns = [ 
	path('three/', views.f33), 
	path('four/', views.f44),
];
