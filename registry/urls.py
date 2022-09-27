from django.urls import path
from registry import views

urlpatterns = [
    path('registry/', views.registry_list),
    path('registry/<int:pk>/', views.registry_detail),
]