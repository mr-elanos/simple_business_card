from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html', {'title': 'Onlyfans | DivaValentina'})


def about(request):
    return render(request, 'pages/about.html', {'title': 'About | DivaValentina'})
