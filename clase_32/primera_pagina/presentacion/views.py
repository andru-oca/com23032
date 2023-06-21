from django.shortcuts import render
from django.views.generic import TemplateView


def LandingPageView(request,nombre):
    extra_context = {
        'nombre_user':nombre
    }
    return render(request,'bloques/landing_page.html',extra_context)



class LandingPageClass(TemplateView):


    template_name = 'bloques/landing_page.html'