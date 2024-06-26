from django.shortcuts import render

def home(request):
    context = {
        'key' : 'value'
    }
    return render(request, 'manabiyacentral/home.html', context)