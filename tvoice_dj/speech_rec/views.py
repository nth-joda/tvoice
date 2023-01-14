from django.http import HttpResponse
from django.template import loader
from speech_rec.models import SpeechFileModel
from speech_rec.serializers import SpeechFileSerializer

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.


def speechRec(request):
    template = loader.get_template('speech_rec.html')
    return HttpResponse(template.render())

class ListCreateSpeechFileView(ListCreateAPIView):
    model = SpeechFileModel
    serializer_class = SpeechFileSerializer

    def get_queryset(self):
        return SpeechFileModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SpeechFileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Upload a new Speech File successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Upload a new Speech File unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteSpeechFileView(RetrieveUpdateDestroyAPIView):
    model = SpeechFileModel
    serializer_class = SpeechFileSerializer

    def put(self, request, *args, **kwargs):
        speechFile = get_object_or_404(SpeechFileModel, id=kwargs.get('pk'))
        serializer = SpeechFileSerializer(speechFile, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Speech File successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Speech File unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        speechFile = get_object_or_404(SpeechFileModel, id=kwargs.get('pk'))
        speechFile.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)
