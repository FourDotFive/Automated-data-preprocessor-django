from django.shortcuts import render
from .forms import FileUploadForm


def main_page_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            print(file)
    file_form = FileUploadForm(request.POST)
    return render(request, 'main.html', context={'file_form': file_form})
