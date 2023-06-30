from django.shortcuts import render
from .forms import FileUploadForm
from .file_reader import read_file, get_df_head, get_delimiter, get_file_name_and_size


def file_uploader_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']
            file_name, file_size = get_file_name_and_size(file)

            if_detect_delimiter = file_form.cleaned_data.get('if_detect_delimiter')
            if if_detect_delimiter:
                delimiter = get_delimiter(file)
            else:
                delimiter = file_form.cleaned_data['delimiter']
            try:
                df = read_file(file, delimiter)

            except ValueError as e:
                return render(request, 'error.html', {'error_message': str(e)})

            else:
                df_head_records_dict = get_df_head(df, number_of_rows=20)
                column_names = df.columns.values

                context = {
                    'file_name': file_name,
                    'file_size': file_size,
                    'column_names': column_names,
                    'df_head_records': df_head_records_dict,
                }
                return render(request, 'data_stats.html', context=context)

    file_form = FileUploadForm(request.POST)
    return render(request, 'uploader.html', context={'file_form': file_form})
