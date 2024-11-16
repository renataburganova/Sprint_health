import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .forms import CSVUploadForm
from .models import SprintData


# Create your views here.

def main(request):
    response = render_to_string('main_page/index.html')
    return HttpResponse(response)


def upload_csv(request):
    if request.method == 'POST' and request.FILES:
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем один файл
            file = request.FILES['file']
            handle_uploaded_file(file)
            return render(request, 'success.html')  # Страница успешной загрузки
    else:
        form = CSVUploadForm()

    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(file):
    # Логика обработки файла, например, чтение CSV
    with open(f'uploaded_files/{file.name}', 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
