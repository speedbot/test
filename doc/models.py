from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

SOURCE_CHOICES = [
    ('.txt', 'Text'),
    ('.doc', 'Document'),
]


class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100)
    source_type = models.CharField(
        choices=SOURCE_CHOICES, blank=True, null=True, max_length=100
    )
    source_id = models.CharField(blank=True, null=True, max_length=20)
    input_meta_data = JSONField(default=dict, null=True, blank=True)