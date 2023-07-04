import datetime
from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadForm
from .file_handler import (
    read_file,
    get_df_head_dict,
    get_delimiter,
    get_file_name_and_size,
    save_file_and_info,
    get_file_name_and_extension,
    read_file_from_temp,
)


def file_uploader_view(request):
    if request.method == 'POST':
        file_form = FileUploadForm(request.POST, request.FILES)
        if file_form.is_valid():
            file = request.FILES['file']

            file_name, file_extension = get_file_name_and_extension(file)
            file_size = get_file_name_and_size(file)

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

                try:
                    folder_name = save_file_and_info(
                        file=file,
                        name=file_name,
                        extension=file_extension,
                        delimiter=delimiter,
                    )
                except OSError:
                    return render(request, 'error.html', {'error_message': 'Please connect with the support'})
                else:
                    df_head_records_dict = get_df_head_dict(df, number_of_rows=20)
                    column_names = df.columns.values

                    context = {
                        'file_name': file_name,
                        'file_size': file_size,
                        'column_names': column_names,
                        'df_head_records': df_head_records_dict,
                        'folder_name': folder_name
                    }
                    return render(request, 'data_stats.html', context=context)

    file_form = FileUploadForm(request.POST)
    return render(request, 'uploader.html', context={'file_form': file_form})


def more_data(request):
    length = 20

    start = int(request.GET.get('start'))
    folder_name = request.GET.get('folder_name')

    df = read_file_from_temp(folder_name)

    next_rows = df[start:start + length].to_dict(orient='index')

    return JsonResponse(next_rows, safe=False)
