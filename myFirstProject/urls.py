from django.urls import path

from . import views

app_name='myFirstProject'

urlpatterns = [
    path('', views.student_view, name='student_view')
]