# accounts/views.py

from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from rest_framework import exceptions

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes=[IsAuthenticated]

    def get_object(self):
        try:
            user_id = self.kwargs['pk']
            is_admin = self.request.user.is_staff
            is_in_magazin_group = self.request.user.groups.filter(name='Magazin').exists()
            if not (user_id == str(self.request.user.id) or is_admin or is_in_magazin_group):
                raise exceptions.PermissionDenied("You do not have permission to access this profile.")
            return UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            raise NotFound("UserProfile not found")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
