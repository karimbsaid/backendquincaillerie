from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Command
from .serializers import CommandSerializer
from .permissions import IsAdminOrMagazinOrReadOnly
class CommandListCreateView(generics.ListCreateAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        data = request.data  
        serializer = self.get_serializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def get_queryset(self):
        is_in_magazin_group = self.request.user.groups.filter(name='Magazin').exists()
        is_admin = self.request.user.is_staff

        if is_admin or is_in_magazin_group:
            # Admins can see all commands
            queryset = Command.objects.all()
        else:
            # Regular users can only see their own commands
            queryset = Command.objects.filter(user=self.request.user)
        param_Startdate=self.request.query_params.get('startDate', None)
        param_Enddate=self.request.query_params.get('endDate', None)
        param_username=self.request.query_params.get('city', None)
        param_category=self.request.query_params.get('category', None)
        if param_category:
            queryset=queryset.filter(product__category=param_category)
        if param_username :

            queryset=queryset.filter(user__username__startswith=param_username)
        
        if param_Startdate!="undefined" and param_Enddate !="undefined":
            start_day =param_Startdate.split('/')[0]
            end_day =param_Enddate.split('/')[0]
            start_month =param_Startdate.split('/')[1]
            end_month =param_Enddate.split('/')[1]
            start_year =param_Startdate.split('/')[2]
            end_year =param_Enddate.split('/')[2]
            queryset=queryset.filter(created_at__month__gte=start_month,
                                     created_at__month__lte=end_month,
                                     created_at__day__gte=start_day,
                                     created_at__day__lte=end_day,
                                     created_at__year__gte=start_year,
                                     created_at__year__lte=end_year)
        return queryset
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        is_in_magazin_group = self.request.user.groups.filter(name='Magazin').exists()
        is_admin = self.request.user.is_staff
        if is_admin or is_in_magazin_group:
            # Admins can see all commands
            return Command.objects.all()
        else:
            # Regular users can only see their own commands
            return Command.objects.filter(user=self.request.user)
