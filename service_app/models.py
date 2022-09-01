from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=35)
    status = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    url = models.SlugField()

    def __str__(self):
        return self.title
