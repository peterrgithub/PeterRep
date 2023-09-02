# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):   #object definition prompt. Where, post is the model name and is case-sensitive (block)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  #
    title = models.CharField(max_length=200)    #setting the number of characters in the tex fields
    text = models.TextField()   #setting blog content
    created_date = models.DateTimeField(default=timezone.now)   #setting the creation date of the post
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title