from django.http import HttpResponse
from django.template.loader import get_template


def home(self):
    plantilla = get_template('index.html')
    return HttpResponse(plantilla.render())

def sistema1(self):
    return HttpResponse('Pagina sistema 1 🔥')
