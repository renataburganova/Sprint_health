from django import forms

class CSVUploadForm(forms.Form):
    # Поле для загрузки одного файла
    file = forms.FileField(
        widget=forms.ClearableFileInput(),
        label='Загрузите файл CSV',
        required=True
    )

