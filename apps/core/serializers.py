from . import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class I011UfSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.I011Uf
        fields = ['id_uf', 'cod_uf',]


class I012MunicipioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.I012Municipio
        fields = '__all__'

class ViewMunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ViewMunicipio
        fields = ['cod_municipio', 'descricao', 'cod_uf']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class I005FilialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.I005Filial
        fields = '__all__'

class I002EmpresaSerializer(serializers.ModelSerializer):
    filiais = serializers.StringRelatedField(many=True)
       
    class Meta:
        model = models.I002Empresa
        fields = ['cod_empresa', 'cnpj', 'razao_social', 'filiais',]