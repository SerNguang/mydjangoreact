# from django.urls import path
# from .views import index

# urlpatterns = [
#     path('', index),
#     path('join', index),
#     path('create', index),
#     path('join/1', index)
# ]

from django.urls import path
from . import views
urlpatterns = [
  path('', views.index)
]