from django.shortcuts import render
from django.shortcuts import render
from property.models import Property
from django.db.models import Count
# Create your views here.


def about(request):

    property_list = Property.objects.all()

    template = 'about/about.html'
    context = {

        'about' : about ,

    }

    return render(request , template , context)
