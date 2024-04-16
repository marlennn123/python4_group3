from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='product_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),

    path('clothes/', ClothesViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('clothes/<int:pk>/', ClothesViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('favorite/', FavoriteViewSet.as_view({'get': 'list',
                                         'post': 'create'}), name='product_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('person/', PersonViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('person/<int:pk>/', PersonViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('news/', NewsViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('news/<int:pk>/', NewsViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('basket/', BasketViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('basket/<int:pk>/', BasketViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('order/', OrderViewSet.as_view({'get': 'list',
                                        'post': 'create'}), name='product_list'),
    path('order/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve',
                                                 'put': 'update', 'delete': 'destroy'}), name='product_list'),
]


