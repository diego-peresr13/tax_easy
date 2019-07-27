from django.shortcuts import render
from . import models
from rest_framework import viewsets
from rest_framework import generics
from . import serializers 
from rest_framework.response import Response
from django.contrib.auth.models import User, Group

# Create your views here.
class I002EmpresaViewSet(viewsets.ModelViewSet):

    queryset = models.I002Empresa.objects.all()
    serializer_class = serializers.I002EmpresaSerializer


class I005FilialViewSet(viewsets.ModelViewSet):

    queryset = models.I005Filial.objects.all()
    serializer_class = serializers.I005FilialSerializer

class I011UfViewSet(viewsets.ModelViewSet):

    queryset = models.I011Uf.objects.all()
    serializer_class = serializers.I011UfSerializer
    

class I012MunicipioList(viewsets.ModelViewSet):

    queryset = models.I012Municipio.objects.select_related('id_uf').all()
    serializer_class = serializers.I012MunicipioSerializer


class ViewMunicipioList(viewsets.ModelViewSet):

    queryset = models.ViewMunicipio.objects.all()
    serializer_class = serializers.ViewMunicipioSerializer



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer