from django.shortcuts import render
from property.models import Property
from django.db.models import Count
from django.http import Http404
# Create your views here.

#

def home(request):

    property_list = Property.objects.all()

    template = 'home/index.html'
    context = {

        'property_list_home' : property_list ,

    }

    return render(request , template , context)
