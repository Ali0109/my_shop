from django.urls import path

from product import views

urlpatterns = [
    path('products/', views.ProductView.as_view()),
    path('product/<int:pk>/', views.ProductView.as_view()),
    path('product/<int:pk>/restore/', views.ProductRestoreAPIView),
]



