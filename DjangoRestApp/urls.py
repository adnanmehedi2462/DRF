from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from DjangoRestApp.views import articallist,crud
from DjangoRestApp import views
urlpatterns = [
	path('articallist/',views.articallist.as_view(),name="articallist"),
	path('crud/<int:pk>/',crud.as_view(),name='crud'),
	

]
