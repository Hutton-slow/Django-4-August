from django.shortcuts import render

def index(request):
    context = {
        'name': 'World',  # This is the dynamic data we'll pass to the template
    }
    return render(request, 'index.html', context)
