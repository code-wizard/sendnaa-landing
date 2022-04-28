from django.urls import path
from landing import views

urlpatterns = [
    path('api/join-list', views.SAJoinListAPIView.as_view())
]