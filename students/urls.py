from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/<str:name>', views.student),
]