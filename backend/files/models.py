from django.db import models
from django.contrib.auth.models import User


class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="files/")
    filename = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.BinaryField()
    iv = models.BinaryField()
    encrypted_key=models.BinaryField()

    def __str__(self):
        return self.filename
  