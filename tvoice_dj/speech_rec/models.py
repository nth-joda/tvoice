from django.db import models

# Create your models here.
class SpeechFileModel(models.Model):
    name = models.CharField(max_length=255) # file name
    extension = models.CharField(max_length=50) # file extension: .wav, .mp3, .mp4
    duration = models.IntegerField() # length of file in seconds 
    size = models.IntegerField() # size of file in bytes
    path = models.CharField(max_length=255) # path to file
    date_created = models.DateTimeField(auto_now_add=True) # date file was created
    date_modified = models.DateTimeField(auto_now=True) # date file was last modified
    file = models.FileField(upload_to='speech_files') # file
    result = models.TextField() # result of speech recognition
    def __str__(self) -> str:
        return self.name + self.extension + "("+self.duration+"s, "+self.size+ "): " + self.result