from django.shortcuts import render


def jared(request):
    return render(request, 'jobs/home.html')
