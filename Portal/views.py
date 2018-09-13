from django.shortcuts import render

# Create your views here.

def infomation(request):
    return render(request, 'Portal/infomation.html')