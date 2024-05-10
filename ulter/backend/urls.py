from django.urls import path
from . import views

urlpatterns=[
    path('data/', views.SensorDataList),
    path('data/<int:pk>/',views.SensorDataDetail.as_view()),
     path('media-content/', views.MediaContentView.as_view()), 
]   