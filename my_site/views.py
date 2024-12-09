from django.http import HttpResponse
from django.template import loader

def base_my_site(request):
    template = loader.get_template('base_my_site.html')
    return HttpResponse(template.render())
