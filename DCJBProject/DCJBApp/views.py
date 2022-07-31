from django.shortcuts import render
from .models import JB_Info

# Create your views here.

def index(request):

    jbs = JB_Info.objects.all()

    return render(request, "index.html", {'jbs': jbs})
