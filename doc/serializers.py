from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Document


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [
            'id', 'owner',  'created_time', 'type', 'source_type', 'source_id', 'input_meta_data',
        ]


