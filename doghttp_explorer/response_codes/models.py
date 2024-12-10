from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ResponseCodeList(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # owner
    created_at = models.DateTimeField(auto_now_add=True)  # date created
    response_codes = models.TextField()  # response codes
    image_links = models.TextField()  # image URLs

    def __str__(self):
        return f"{self.name} - {self.user.username}"