from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.FlowerListView.as_view(), name='flower_list_api'),
    path('flowers/<int:pk>/', views.FlowerDetailView.as_view(), name='flower_detail_api'),
]
