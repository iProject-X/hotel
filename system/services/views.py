from django.shortcuts import render
from django.shortcuts import render
from property.models import Property
from django.db.models import Count
# Create your views here.


def services(request):

    property_list = Property.objects.all()

    template = 'services/services.html'
    context = {

        'services' : services ,

    }

    return render(request , template , context)
