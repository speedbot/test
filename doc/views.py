import json

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer, DocumentSerializer
from .models import Document
from .forms import DocumentForm


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class DocumentViewSet(viewsets.ModelViewSet):

    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj:
            obj.delete()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)

    def create(self, request, *args, **kwargs):
        user_id = request.POST.get('user_id', None)
        type = request.POST.get('type', None)
        source_type = request.POST.get('source_type', None)
        source_id = request.POST.get('source_id', None)
        input_metadata = json.dumps(
            request.POST.get('input_metadata', None),
        )
        data = {
            'owner': user_id,
            'type': type,
            'source_type': source_type,
            'source_id': source_id,
            'input_metadata': input_metadata
        }
        form = DocumentForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return Response(form.errors)
