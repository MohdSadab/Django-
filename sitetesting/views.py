from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import add
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from .serializers import SitesSerializer
from .models import Sites


# Create your views here.
def Home(request,x,y):
    add.delay(x,y)
    print(x,y)

    return HttpResponse({"ok":True})


class Sites(viewsets.ModelViewSet):
    serializer_class=SitesSerializer
    queryset=Sites.objects.all()
    

