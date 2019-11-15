from django.shortcuts import render

from .models import Property
from .form import ReserveForm

from django.http import HttpResponse
from django.views.generic.base import View



def property_list(request, ):
    property_list = Property.objects.all()
    template = 'property/list.html'
    contex = {
        'property_list' : property_list
    }


    if request.method == 'POST':
        reseve_form =ReserveForm(request.POST)
        if reseve_form.is_valid():
            print('Спасибо!')
    else:
        reseve_form = ReserveForm()

    return render(request, template, contex)

def property_detail(request, id):
    property_detail = Property.objects.get('')
    template = 'property/base.html'
    context = {
    'property_detail' : property_detail
    }
    return render(request, template, context)
