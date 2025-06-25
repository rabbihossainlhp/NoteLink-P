from django.db import models
from users.models import CustomUser

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    file_upload = models.FileField(upload_to='media/notes/notes_file', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title