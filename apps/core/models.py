# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class I001GrupoCorp(models.Model):
    id_grupo_corp = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'i001_grupo_corp'


class I002Empresa(models.Model):
    id_empresa = models.BigIntegerField(primary_key=True)
    id_grupo_corp = models.ForeignKey(I001GrupoCorp, models.DO_NOTHING, db_column='id_grupo_corp')
    cod_empresa = models.CharField(max_length=9)
    cnpj = models.CharField(max_length=14)
    razao_social = models.CharField(max_length=255)
    chave_licenca = models.CharField(max_length=255, blank=True, null=True)
    data_fim_licenca = models.DateField(blank=True, null=True)
    ativo = models.CharField(max_length=1, blank=True, null=True)
    qtde_filiais = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'i002_empresa'
    
    def __str__(self):
        return self.cod_empresa


class I005Filial(models.Model):
    empresa = models.ForeignKey(I002Empresa, related_name='filiais', on_delete=models.PROTECT)
    id_filial = models.BigIntegerField(primary_key=True)
    cod_filial = models.CharField(max_length=6)
    razao_social = models.CharField(max_length=60)
    matriz_filial = models.CharField(max_length=1, blank=True, null=True)
    cnpj = models.CharField(max_length=14)
    nire = models.CharField(max_length=14, blank=True, null=True)
    cnae = models.CharField(max_length=7, blank=True, null=True)
    inscr_estadual = models.CharField(max_length=14)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    num_endereco = models.CharField(max_length=10, blank=True, null=True)
    compl_endereco = models.CharField(max_length=60, blank=True, null=True)
    bairro = models.CharField(max_length=60, blank=True, null=True)
    id_uf = models.ForeignKey('I011Uf', models.DO_NOTHING, db_column='id_uf')
    cep = models.CharField(max_length=8, blank=True, null=True)
    data_abertura = models.DateField(blank=True, null=True)
    ativo = models.CharField(max_length=1)
    id_municipio = models.ForeignKey('I012Municipio', models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i005_filial'

    def __str__(self):
        return '%s: %s' % (self.cod_filial, self.razao_social)

class I011Uf(models.Model):
    id_uf = models.BigIntegerField(primary_key=True)
    cod_uf = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'i011_uf'
    
    def __str__(self):
        return self.cod_uf


class I012Municipio(models.Model):
    id_municipio = models.BigIntegerField(primary_key=True)
    cod_municipio = models.CharField(max_length=7)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    id_uf = models.ForeignKey(I011Uf, related_name='uf', on_delete=models.PROTECT, db_column='id_uf')

    class Meta:
        managed = False
        db_table = 'i012_municipio'

    def __str__(self):
        return self.cod_municipio


class I013PlanoContas(models.Model):
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')
    cod_conta = models.CharField(primary_key=True, max_length=70)
    ind_conta = models.CharField(max_length=1)
    descricao_conta = models.CharField(max_length=255)
    nivel = models.CharField(max_length=2)
    cod_conta_sintetica = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i013_plano_contas'
        unique_together = (('cod_conta', 'id_empresa'),)

    def __str__(self):
        return self.cod_conta


class I014Categoria(models.Model):
    id_categoria = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i014_categoria'


class I015Imposto(models.Model):    
    id_imposto = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    id_categoria = models.ForeignKey(I014Categoria, models.DO_NOTHING, db_column='id_categoria')
    cod_imposto = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'i015_imposto'

class ViewMunicipio(models.Model):    
    cod_municipio = models.CharField(max_length=7)
    descricao = models.CharField(max_length=255)
    cod_uf = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'view_municipio'