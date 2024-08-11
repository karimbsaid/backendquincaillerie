from django.urls import path , include
from . import views
urlpatterns = [
    path('product', views.ProductListView.as_view()),
    path('product/<int:pk>', views.ProductSingleView.as_view())
]