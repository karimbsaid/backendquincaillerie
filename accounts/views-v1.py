# accounts/views.py

from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]
    def get_object(self):
        # Use the user ID to get the UserProfile
        try:
            return UserProfile.objects.get(user_id=self.kwargs['pk'])
        except UserProfile.DoesNotExist:
            raise NotFound("UserProfile not found")
    def update(self, request, *args, **kwargs):
        # Get the user profile instance
        instance = self.get_object()
        
        # Perform any custom logic here (e.g., logging, validation)
        print(f"User ID: {request.user.id} is updating profile ID: {instance.id}")
        
        # Partially update the instance with the new data
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        
        # Validate the serializer
        serializer.is_valid(raise_exception=True)
        
        # Save the updated instance
        self.perform_update(serializer)
        
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
