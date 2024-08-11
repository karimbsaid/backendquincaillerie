# urls.py

from django.urls import path
from .views import UserGroupsAPIView

urlpatterns = [
    path('user-groups', UserGroupsAPIView.as_view(), name='user-groups'),
    # Add other URLs as needed
]
