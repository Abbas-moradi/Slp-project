from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.RegisterQuestion.as_view(), name='question_register'),
]