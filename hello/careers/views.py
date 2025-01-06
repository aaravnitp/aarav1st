from django.template import loader

from django.http import HttpResponse

def career(request):
    template = loader.get_template('career.html')
    return HttpResponse(template.render())
