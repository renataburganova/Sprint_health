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


# Функции для получения команд, метрик и спринтов из питоновского файла
def get_team_data():
    # Пример функции, которая может быть использована для получения данных команд
    return ["Команда 1", "Команда 2", "Команда 3"]


def get_metrics_data():
    # Пример функции, которая может быть использована для получения данных метрик
    return ["Метрика 1", "Метрика 2", "Метрика 3"]


def get_sprint_data():
    # Пример функции, которая может быть использована для получения данных спринтов
    return ["Спринт 1", "Спринт 2", "Спринт 3"]


def my_view(request):
    teams = get_team_data()
    metrics = get_metrics_data()
    sprints = get_sprint_data()

    # Передаем данные в шаблон
    return render(request, 'index.html', {'teams': teams, 'metrics': metrics, 'sprints': sprints})
