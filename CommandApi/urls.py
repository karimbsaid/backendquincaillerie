from django.urls import path
from .views import CommandListCreateView, CommandDetailView

urlpatterns = [
    path('commands/', CommandListCreateView.as_view(), name='command-list-create'),
    path('commands/<int:pk>/', CommandDetailView.as_view(), name='command-detail'),
]
