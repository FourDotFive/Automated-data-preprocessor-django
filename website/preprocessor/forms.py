from django import forms
from django.core.exceptions import ValidationError


class FileUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={"class": "file-input", "accept": ".csv,.txt"}
        )
    )
    delimiter = forms.CharField(required=True)
