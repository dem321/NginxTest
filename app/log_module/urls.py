from django.urls import path

from log_module.views import LogView

urlpatterns = [
    path('log/', LogView.as_view({'get': 'list', 'post': 'create'}), name='log'),
    path('log/<int:pk>/',
         LogView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'put': 'update'}),
         name='log'),
]