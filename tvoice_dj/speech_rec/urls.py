from django.urls import path
from . import views

urlpatterns = [
    path('speech-rec/', views.ListCreateSpeechFileView.as_view()),
    path('speech-rec/<int:pk>', views.UpdateDeleteSpeechFileView.as_view()),
]