from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.

def main(request):
    response = render_to_string('main_page/index.html')
    return HttpResponse(response)
