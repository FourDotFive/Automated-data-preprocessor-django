from django.shortcuts import render
from .forms import FileUploadForm
from .data_analysis import read_file


def file_uploader_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            delimiter = file_form.cleaned_data['delimiter']
            print(delimiter)
            try:
                read_file(file, delimiter)
                return render(request, 'success.html')
            except ValueError as e:
                return render(request, 'error.html', {'error_message': str(e)})

    file_form = FileUploadForm(request.POST)
    return render(request, 'uploader.html', context={'file_form': file_form})
