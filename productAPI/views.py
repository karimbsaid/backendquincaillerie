from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import ProductList
from .serializers import ProductListeSerializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from .permissions import ProductApiPermission

class ProductListPagination(PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })

class ProductListView(generics.ListCreateAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductListeSerializers
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [ProductApiPermission]
    pagination_class = ProductListPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        param_category = self.request.query_params.get('category', None)
        param_name = self.request.query_params.get('search', None)
        
        if param_category:
            queryset = queryset.filter(category=param_category)
        if param_name:
            queryset = queryset.filter(name__startswith=param_name)
       
        return queryset

class ProductSingleView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = ProductList.objects.all()
    serializer_class = ProductListeSerializers

    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [ProductApiPermission]
