from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=35)
    status = models.CharField(max_length=30)
    created_at = models.DateField(auto_now_add=True)
    message = models.TextField()
    url = models.SlugField()
    email = models.EmailField(max_length=255, null=True)
    notification_group = models.CharField(verbose_name='notification_group', max_length=255, null=True)

    def __str__(self):
        return self.title