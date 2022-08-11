from django.http import HttpResponse
import datetime

def current_datetime(request): # El nombre puede ser cualquiera
    now = datetime.datetime.now()
    html = "<html><body>La Fecha y Hora Actual %s.</body></html>"% now
    return HttpResponse(html)
