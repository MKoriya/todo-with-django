from django.db import models
from django.contrib.auth.models import User

class notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created =  models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title