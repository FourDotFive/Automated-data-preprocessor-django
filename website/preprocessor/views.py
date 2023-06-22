from django.shortcuts import render
from .forms import FileUploadForm
from .data_analysis import read_file, analyse_df


def file_uploader_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            if_detect_delimiter = file_form.cleaned_data.get('if_detect_delimiter')
            delimiter = file_form.cleaned_data['delimiter']
            # print(delimiter)
            try:
                df = read_file(file)
                df_head = analyse_df(df)
                df_html = df_head.to_html()
                context = {
                    'df_html': df_html
                }
                return render(request, 'data_stats.html', context=context)
            except ValueError as e:
                return render(request, 'error.html', {'error_message': str(e)})

    file_form = FileUploadForm(request.POST)
    return render(request, 'uploader.html', context={'file_form': file_form})
