from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def intro(request):
    return render(request, 'intro/introduction.html')


def details(request):
    address = ''
    print('option value: ',request.GET.get('city'))
    if request.GET.get('city') == 'gandhinagar':
        address = 'Sargasan,Gandhinagar'

    if request.GET.get('city') == 'dhanera':
        address = 'Dhakha gate,Dhanera'


    return render(request,'intro/details.html',{'add' : address})

def about(request):
    return render(request, 'intro/about.html')