from django import forms
from django.core.exceptions import ValidationError


class FileUploadForm(forms.Form):
    file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(
            attrs={"class": "file-input", "accept": ".csv,.txt"}
        )
    )
    if_detect_delimiter = forms.BooleanField(
        required=False,
        label='Detect CSV delimiter',
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        )
    )
    delimiter = forms.CharField(required=True)
