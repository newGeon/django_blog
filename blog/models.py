from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
"""
class UserInfo(models.Model):
    user_id = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)
    state = models.CharField(max_length=3, blank=True, null=True)
    role = models.CharField(max_length=3, blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)
    cretaed_date = models.DateField()
    modify_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'user_info'
"""