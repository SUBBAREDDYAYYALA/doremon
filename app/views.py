from django.shortcuts import render

# Create your views here.
def doremon(request):
    return render(request,'doremon.html')