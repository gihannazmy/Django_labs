from django.urls import path
from .views import *

urlpatterns = [
    path('',tracks_list,name='tracks_list'),
    path('Track/create',track_create,name='track_create'),
    path('Tracks/update/<int:id>',track_update,name='track_update'),
    path('Tracks/details/<int:id>',track_details,name='track_details'),
    path('Tracks/delete/<int:id>',track_delete,name='track_delete'),
]
