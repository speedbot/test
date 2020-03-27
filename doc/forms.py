from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('owner', 'type', 'source_type', 'source_id', 'input_meta_data')