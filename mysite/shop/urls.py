from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list',
                                 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                          'put': 'update', 'delete': 'destroy'}), name='product_detail'),

    path('marka/', CategoryViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('marka/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),

    path('model/', ClothesViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('model/<int:pk>/', ClothesViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('category/', FavoriteViewSet.as_view({'get': 'list',
                                         'post': 'create'}), name='product_list'),
    path('category/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('bet/', PersonViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('bet/<int:pk>/', PersonViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('bet/', NewsViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('bet/<int:pk>/', NewsViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('bet/', BasketViewSet.as_view({'get': 'list',
                                             'post': 'create'}), name='product_list'),
    path('bet/<int:pk>/', BasketViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update', 'delete': 'destroy'}), name='product_list'),
    path('bet/', OrderViewSet.as_view({'get': 'list',
                                        'post': 'create'}), name='product_list'),
    path('bet/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve',
                                                 'put': 'update', 'delete': 'destroy'}), name='product_list'),
]


