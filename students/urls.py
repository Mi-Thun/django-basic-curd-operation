from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/<str:name>', views.student),
    path('add_student/', views.add_student, name='add_student'),
]