from django.shortcuts import render
from django.shortcuts import render
from property.models import Property
from django.db.models import Count
# Create your views here.


def contact(request):

    property_list = Property.objects.all()

    template = 'contact/contact.html'
    context = {

        'contact' : contact ,

    }

    return render(request , template , context)
