from rest_framework import serializers
from speech_rec.models import SpeechFileModel

class SpeechFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechFileModel
        fields = ('name', 'extension', 'duration', 'size', 'path',  'date_created', 'date_modified','file', 'result')