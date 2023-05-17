from django.urls import path
from . import views
from . import algorithm

urlpatterns = [
    path('', views.spam_or_ham),
]

