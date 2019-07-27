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


class I003Modulo(models.Model):
    id_modulo = models.BigIntegerField(primary_key=True)
    nome_modulo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i003_modulo'


class I004EmpresaModulo(models.Model):
    id_empr_modulo = models.BigIntegerField(primary_key=True)
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_modulo = models.ForeignKey(I003Modulo, models.DO_NOTHING, db_column='id_modulo')

    class Meta:
        managed = False
        db_table = 'i004_empresa_modulo'


class I005Filial(models.Model):
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')
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
        unique_together = (('id_filial', 'id_empresa'),)


class I006GrupoAcesso(models.Model):
    id_grupo_acesso = models.BigIntegerField(primary_key=True)
    nome_grupo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i006_grupo_acesso'


class I007GrupoModulo(models.Model):
    id_modulo = models.ForeignKey(I003Modulo, models.DO_NOTHING, db_column='id_modulo')
    id_grupo_acesso = models.ForeignKey(I006GrupoAcesso, models.DO_NOTHING, db_column='id_grupo_acesso')
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'i007_grupo_modulo'


class I008GrupoFilial(models.Model):
    id_filial = models.BigIntegerField()
    id_grupo_acesso = models.ForeignKey(I006GrupoAcesso, models.DO_NOTHING, db_column='id_grupo_acesso')

    class Meta:
        managed = False
        db_table = 'i008_grupo_filial'


class I009GrupoEmpresa(models.Model):
    id_grupo_acesso = models.ForeignKey(I006GrupoAcesso, models.DO_NOTHING, db_column='id_grupo_acesso')
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')

    class Meta:
        managed = False
        db_table = 'i009_grupo_empresa'


class I010Usuario(models.Model):
    id_usuario = models.BigIntegerField(primary_key=True)
    nome_usuario = models.CharField(max_length=255)
    num_cpf = models.CharField(max_length=70, blank=True, null=True)
    login = models.CharField(max_length=70)
    senha = models.CharField(max_length=70)
    email = models.CharField(max_length=60)
    id_grupo_acesso = models.ForeignKey(I006GrupoAcesso, models.DO_NOTHING, db_column='id_grupo_acesso')
    dt_ultimo_acesso = models.DateField(blank=True, null=True)
    dt_criacao = models.DateField(blank=True, null=True)
    dt_expira = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    resp_licenca = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i010_usuario'


class I011Uf(models.Model):
    id_uf = models.BigIntegerField(primary_key=True)
    cod_uf = models.CharField(max_length=2)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'i011_uf'


class I012Municipio(models.Model):
    id_municipio = models.BigIntegerField(primary_key=True)
    cod_municipio = models.CharField(max_length=7)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    id_uf = models.ForeignKey(I011Uf, models.DO_NOTHING, db_column='id_uf')

    class Meta:
        managed = False
        db_table = 'i012_municipio'


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
    id_imposto_macro = models.ForeignKey('I021ImpostoMacro', models.DO_NOTHING, db_column='id_imposto_macro', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i015_imposto'


class I016CodDarf(models.Model):
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    cod_darf = models.CharField(max_length=6)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i016_cod_darf'


class I017ConfigIni(models.Model):
    id_config = models.BigIntegerField(primary_key=True)
    id_grupo_corp = models.ForeignKey(I001GrupoCorp, models.DO_NOTHING, db_column='id_grupo_corp')
    ind_instance = models.CharField(max_length=1, blank=True, null=True)
    owner_bd_origem = models.CharField(max_length=20)
    dblink = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'i017_config_ini'


class I018ClassPend(models.Model):
    id_class = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'i018_class_pend'


class I019Cst(models.Model):
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto', primary_key=True)
    cst = models.CharField(max_length=3)
    descricao = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'i019_cst'
        unique_together = (('id_imposto', 'cst'),)


class I020RelacCst(models.Model):
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')
    id_imposto = models.ForeignKey(I019Cst, models.DO_NOTHING, db_column='id_imposto')
    cst = models.ForeignKey(I019Cst, models.DO_NOTHING, db_column='cst', primary_key=True)

    class Meta:
        managed = False
        db_table = 'i020_relac_cst'
        unique_together = (('cst', 'id_empresa', 'id_imposto'),)


class I021ImpostoDet(models.Model):
    id_imposto_det = models.BigIntegerField(primary_key=True)
    cod_imposto = models.CharField(max_length=10)
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    movto = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'i021_imposto_det'


class I021ImpostoMacro(models.Model):
    id_imposto_macro = models.BigIntegerField(primary_key=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i021_imposto_macro'


class I100Lancamentos(models.Model):
    id_lancamento = models.CharField(primary_key=True, max_length=50)
    num_lancto = models.CharField(max_length=40)
    id_empresa = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    cod_conta = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='cod_conta')
    data_lancto = models.DateField()
    num_arq = models.CharField(max_length=100)
    vlr_lancto = models.DecimalField(max_digits=19, decimal_places=2)
    ind_dc = models.CharField(max_length=1)
    ind_lancto = models.CharField(max_length=1)
    tipo_lancto = models.CharField(max_length=2, blank=True, null=True)
    num_lancto_comp = models.CharField(max_length=40, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)
    num_docto = models.CharField(max_length=12, blank=True, null=True)
    cod_parceiro = models.CharField(max_length=14, blank=True, null=True)
    cnpj_parceiro = models.CharField(max_length=14, blank=True, null=True)
    aux01 = models.CharField(max_length=10, blank=True, null=True)
    aux02 = models.CharField(max_length=20, blank=True, null=True)
    aux03 = models.CharField(max_length=20, blank=True, null=True)
    aux04 = models.CharField(max_length=20, blank=True, null=True)
    aux05 = models.CharField(max_length=20, blank=True, null=True)
    aux06 = models.CharField(max_length=20, blank=True, null=True)
    ind_integracao = models.CharField(max_length=1)
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')

    class Meta:
        managed = False
        db_table = 'i100_lancamentos'


class I101Saldos(models.Model):
    id_saldo = models.CharField(primary_key=True, max_length=50)
    id_empresa = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    periodo = models.DateField()
    cod_conta = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='cod_conta')
    vlr_saldo_ini = models.DecimalField(max_digits=17, decimal_places=2)
    ind_deb_cred_ini = models.CharField(max_length=1)
    vlr_saldo_fim = models.DecimalField(max_digits=17, decimal_places=2)
    ind_deb_cred_fim = models.CharField(max_length=1)
    vlr_tot_cred = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    vlr_tot_deb = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    ind_contab_fiscal = models.CharField(max_length=1)
    ind_integracao = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'i101_saldos'


class I200NotaFiscal(models.Model):
    id_nf = models.CharField(primary_key=True, max_length=50)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    ind_oper = models.CharField(max_length=1)
    ind_emissao = models.CharField(max_length=1)
    ind_tipo_nf = models.CharField(max_length=1)
    data_emissao = models.DateField()
    data_e_s = models.DateField()
    num_nf = models.CharField(max_length=12)
    serie = models.CharField(max_length=3)
    norm_dev = models.CharField(max_length=1)
    chave_nfe = models.CharField(max_length=44, blank=True, null=True)
    tp_docto = models.CharField(max_length=10)
    descr_tp_docto = models.CharField(max_length=100, blank=True, null=True)
    modelo_nf = models.CharField(max_length=10, blank=True, null=True)
    ind_situacao = models.CharField(max_length=1, blank=True, null=True)
    ind_nf_manual = models.CharField(max_length=1, blank=True, null=True)
    vlr_nf = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    vlr_merc_serv = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    num_lancto = models.CharField(max_length=40, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)
    cod_parceiro = models.CharField(max_length=14)
    cnpj_parceiro = models.CharField(max_length=14, blank=True, null=True)
    razao_social = models.CharField(max_length=100, blank=True, null=True)
    inscr_estadual = models.CharField(max_length=14, blank=True, null=True)
    aux01 = models.CharField(max_length=10, blank=True, null=True)
    aux02 = models.CharField(max_length=20, blank=True, null=True)
    aux03 = models.CharField(max_length=20, blank=True, null=True)
    aux04 = models.CharField(max_length=20, blank=True, null=True)
    aux05 = models.CharField(max_length=20, blank=True, null=True)
    aux06 = models.CharField(max_length=20, blank=True, null=True)
    ind_integracao = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'i200_nota_fiscal'


class I201NfItem(models.Model):
    id_nf = models.ForeignKey(I200NotaFiscal, models.DO_NOTHING, db_column='id_nf', primary_key=True)
    cod_item = models.CharField(max_length=35)
    descricao_item = models.CharField(max_length=100, blank=True, null=True)
    cod_ncm = models.CharField(max_length=10, blank=True, null=True)
    descr_ncm = models.CharField(max_length=100, blank=True, null=True)
    num_item = models.BigIntegerField()
    cfop = models.CharField(max_length=4, blank=True, null=True)
    descr_cfop = models.CharField(max_length=100, blank=True, null=True)
    nat_op = models.CharField(max_length=3, blank=True, null=True)
    descr_nat_op = models.CharField(max_length=100, blank=True, null=True)
    cod_medida = models.CharField(max_length=3, blank=True, null=True)
    vlr_item = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_contabil_item = models.DecimalField(max_digits=17, decimal_places=2)
    num_pedido = models.CharField(max_length=30, blank=True, null=True)
    cod_lei_116 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i201_nf_item'
        unique_together = (('id_nf', 'num_item'),)


class I202ItemImposto(models.Model):
    id_nf = models.ForeignKey(I201NfItem, models.DO_NOTHING, db_column='id_nf', primary_key=True)
    num_item = models.ForeignKey(I201NfItem, models.DO_NOTHING, db_column='num_item')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    ind_tributacao = models.CharField(max_length=1)
    vlr_base = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_aliq = models.DecimalField(max_digits=7, decimal_places=4)
    vlr_tributo = models.DecimalField(max_digits=17, decimal_places=2)
    cst = models.CharField(max_length=2, blank=True, null=True)
    cod_imposto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i202_item_imposto'
        unique_together = (('id_nf', 'num_item', 'id_imposto', 'ind_tributacao'),)


class I203Ativo(models.Model):
    id_docto_ativo = models.CharField(primary_key=True, max_length=50)
    tipo_docto = models.CharField(max_length=10)
    data_parcela = models.DateField()
    num_parcela = models.BigIntegerField(blank=True, null=True)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    num_lancto = models.CharField(max_length=40, blank=True, null=True)
    vlr_operacao = models.DecimalField(max_digits=17, decimal_places=2)
    cst = models.CharField(max_length=2)
    vlr_base = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_aliquota = models.DecimalField(max_digits=7, decimal_places=4)
    vlr_tributo = models.DecimalField(max_digits=17, decimal_places=2)
    cod_imposto = models.CharField(max_length=10, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i203_ativo'


class I204OutrosDoctos(models.Model):
    id_docto = models.CharField(primary_key=True, max_length=50)
    data_docto = models.DateField(blank=True, null=True)
    tipo_docto = models.CharField(max_length=10)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    num_docto = models.CharField(max_length=12, blank=True, null=True)
    serie_docto = models.CharField(max_length=3, blank=True, null=True)
    num_lancto = models.CharField(max_length=40, blank=True, null=True)
    vlr_operacao = models.DecimalField(max_digits=17, decimal_places=2)
    cst = models.CharField(max_length=2)
    vlr_base = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_aliquota = models.DecimalField(max_digits=7, decimal_places=4)
    vlr_tributo = models.DecimalField(max_digits=17, decimal_places=2)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    cod_imposto = models.CharField(max_length=10, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i204_outros_doctos'


class I210Retencoes(models.Model):
    id_docto = models.CharField(primary_key=True, max_length=50)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    movto = models.CharField(max_length=1, blank=True, null=True)
    cod_darf = models.CharField(max_length=6)
    docnum = models.CharField(max_length=12, blank=True, null=True)
    num_docto = models.CharField(max_length=12)
    data_docto = models.DateField()
    serie_docto = models.CharField(max_length=3)
    data_fato_gerador = models.DateField()
    tp_docto = models.CharField(max_length=10, blank=True, null=True)
    desc_tp_docto = models.CharField(max_length=100, blank=True, null=True)
    num_lancto = models.CharField(max_length=40, blank=True, null=True)
    num_lancto_comp = models.CharField(max_length=40, blank=True, null=True)
    cod_parceiro = models.CharField(max_length=14)
    cnpj_parceiro = models.CharField(max_length=14, blank=True, null=True)
    razao_social = models.CharField(max_length=100, blank=True, null=True)
    insc_estadual = models.CharField(max_length=14, blank=True, null=True)
    vlr_docto = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_aliq = models.DecimalField(max_digits=7, decimal_places=4)
    vlr_retencao = models.DecimalField(max_digits=17, decimal_places=2)
    ind_docto_manual = models.CharField(max_length=1, blank=True, null=True)
    aux01 = models.CharField(max_length=10, blank=True, null=True)
    aux02 = models.CharField(max_length=20, blank=True, null=True)
    aux03 = models.CharField(max_length=20, blank=True, null=True)
    aux04 = models.CharField(max_length=20, blank=True, null=True)
    aux05 = models.CharField(max_length=20, blank=True, null=True)
    aux06 = models.CharField(max_length=20, blank=True, null=True)
    ind_integracao = models.CharField(max_length=1, blank=True, null=True)
    cod_imposto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i210_retencoes'


class I220LanctoApuracao(models.Model):
    id_lancto_apuracao = models.CharField(primary_key=True, max_length=50)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    data_apur = models.DateField()
    cod_oper_apur = models.CharField(max_length=3)
    desc_oper_apur = models.CharField(max_length=50)
    sequencial = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    vlr_apur = models.DecimalField(max_digits=17, decimal_places=2)
    ind_integracao = models.CharField(max_length=1)
    cod_ajuste = models.CharField(max_length=20, blank=True, null=True)
    cod_livro = models.CharField(max_length=3)
    cod_imposto = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i220_lancto_apuracao'


class I221GuiaPagamento(models.Model):
    id_guia = models.BigIntegerField(primary_key=True)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    data_apur = models.DateField(blank=True, null=True)
    data_pagto = models.DateField(blank=True, null=True)
    num_guia = models.IntegerField(blank=True, null=True)
    descricao = models.CharField(max_length=50, blank=True, null=True)
    vlr_guia = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    vlr_residual = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_baixado = models.DecimalField(max_digits=17, decimal_places=2)
    ind_integracao = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'i221_guia_pagamento'


class I222GuiaItem(models.Model):
    id_guia = models.ForeignKey(I221GuiaPagamento, models.DO_NOTHING, db_column='id_guia')
    num_docto = models.CharField(max_length=12)
    data_docto = models.DateField(blank=True, null=True)
    valor_docto = models.DecimalField(max_digits=17, decimal_places=2)
    id_utilizado = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i222_guia_item'


class I500ParamConta(models.Model):
    id_empresa = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='id_empresa', primary_key=True)
    cod_conta = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='cod_conta')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    movto = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'i500_param_conta'
        unique_together = (('id_empresa', 'cod_conta', 'id_imposto', 'movto'),)


class I501ParamConcLevel(models.Model):
    id_conc_level = models.BigIntegerField(primary_key=True)
    id_empresa = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.ForeignKey(I005Filial, models.DO_NOTHING, db_column='id_filial')
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    ind_level = models.BigIntegerField()
    vlr_lancto = models.DecimalField(max_digits=17, decimal_places=2)
    field1 = models.CharField(max_length=30, blank=True, null=True)
    field2 = models.CharField(max_length=30, blank=True, null=True)
    field3 = models.CharField(max_length=30, blank=True, null=True)
    field4 = models.CharField(max_length=30, blank=True, null=True)
    field5 = models.CharField(max_length=30, blank=True, null=True)
    field6 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i501_param_conc_level'


class I800Conciliacao(models.Model):
    id_conciliacao = models.BigIntegerField(primary_key=True)
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    periodo = models.DateField()
    id_empresa = models.ForeignKey(I002Empresa, models.DO_NOTHING, db_column='id_empresa')
    usuario = models.CharField(max_length=35)
    data_criacao = models.DateField()
    ind_status = models.CharField(max_length=1)
    control = models.CharField(max_length=40, blank=True, null=True)
    equalizar_contabil = models.CharField(max_length=1, blank=True, null=True)
    equalizar_fiscal = models.CharField(max_length=1, blank=True, null=True)
    rec_conc_manual = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i800_conciliacao'
        unique_together = (('id_imposto', 'periodo', 'id_empresa'),)


class I801ConciliacaoDet(models.Model):
    id_conciliacao = models.ForeignKey(I800Conciliacao, models.DO_NOTHING, db_column='id_conciliacao', primary_key=True)
    id_lancamento = models.CharField(max_length=50)
    id_docto = models.CharField(max_length=50)
    cod_conta = models.CharField(max_length=70)
    periodo = models.DateField()
    origem = models.CharField(max_length=4)
    ind_conciliado = models.CharField(max_length=1)
    ind_nivel = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i801_conciliacao_det'
        unique_together = (('id_conciliacao', 'id_lancamento', 'id_docto', 'cod_conta', 'periodo', 'origem'),)


class I802LanctoProc(models.Model):
    id_lancamento = models.CharField(max_length=50)
    id_empresa = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='id_empresa')
    id_filial = models.BigIntegerField()
    num_lancto = models.CharField(max_length=60)
    ind_deb_cred = models.CharField(max_length=1, blank=True, null=True)
    cod_conta = models.ForeignKey(I013PlanoContas, models.DO_NOTHING, db_column='cod_conta')
    vlr_lancto_residual = models.DecimalField(max_digits=17, decimal_places=2)
    vlr_lancto_original = models.DecimalField(max_digits=17, decimal_places=2, blank=True, null=True)
    data_lancto = models.DateField()
    justificativa = models.CharField(max_length=255, blank=True, null=True)
    id_class = models.ForeignKey(I018ClassPend, models.DO_NOTHING, db_column='id_class', blank=True, null=True)
    id_imposto = models.BigIntegerField()
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i802_lancto_proc'
        unique_together = (('id_lancamento', 'num_lancto', 'ind_deb_cred', 'cod_conta', 'data_lancto', 'id_empresa', 'id_conciliacao'),)


class I803DoctoProc(models.Model):
    id_documento = models.CharField(max_length=50, blank=True, null=True)
    id_empresa = models.BigIntegerField()
    id_filial = models.BigIntegerField()
    num_docto = models.CharField(max_length=12, blank=True, null=True)
    data_docto = models.DateField()
    movto = models.CharField(max_length=1)
    vlr_lancto = models.DecimalField(max_digits=17, decimal_places=2)
    origem = models.CharField(max_length=4)
    num_lancto = models.CharField(max_length=60, blank=True, null=True)
    cod_conta = models.CharField(max_length=70)
    id_imposto = models.ForeignKey(I015Imposto, models.DO_NOTHING, db_column='id_imposto')
    justificativa = models.CharField(max_length=255, blank=True, null=True)
    id_class = models.ForeignKey(I018ClassPend, models.DO_NOTHING, db_column='id_class', blank=True, null=True)
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    docnum = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i803_docto_proc'
        unique_together = (('id_documento', 'num_docto', 'data_docto', 'movto', 'origem', 'num_lancto', 'id_imposto', 'id_filial', 'id_empresa', 'id_conciliacao'),)


class I804AppConciliacao(models.Model):
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    id_lancamento = models.CharField(max_length=50, blank=True, null=True)
    id_docto = models.CharField(max_length=50, blank=True, null=True)
    id_imposto = models.BigIntegerField(blank=True, null=True)
    ind_parcial = models.CharField(max_length=1, blank=True, null=True)
    origem = models.CharField(max_length=10, blank=True, null=True)
    processo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i804_app_conciliacao'


class I804TmpConciliacao(models.Model):
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    id_lancamento = models.CharField(max_length=50, blank=True, null=True)
    id_docto = models.CharField(max_length=50, blank=True, null=True)
    id_imposto = models.BigIntegerField(blank=True, null=True)
    ind_parcial = models.CharField(max_length=1, blank=True, null=True)
    origem = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i804_tmp_conciliacao'


class I900ProcessoLog(models.Model):
    num_processo = models.BigIntegerField(primary_key=True)
    msg_erro = models.CharField(max_length=255, blank=True, null=True)
    processo = models.CharField(max_length=255, blank=True, null=True)
    erro_db = models.CharField(max_length=255, blank=True, null=True)
    id_usuario = models.ForeignKey(I010Usuario, models.DO_NOTHING, db_column='id_usuario')
    data_processo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i900_processo_log'


class I901ReprocConciliacao(models.Model):
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    id_empresa = models.BigIntegerField(blank=True, null=True)
    id_lancamento = models.CharField(max_length=50, blank=True, null=True)
    id_docto = models.CharField(max_length=50, blank=True, null=True)
    id_imposto = models.BigIntegerField(blank=True, null=True)
    cod_conta = models.CharField(max_length=70, blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)
    origem = models.CharField(max_length=4, blank=True, null=True)
    ind_conciliado = models.CharField(max_length=1, blank=True, null=True)
    ind_nivel = models.CharField(max_length=2, blank=True, null=True)
    ind_parcial = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i901_reproc_conciliacao'


class I902ProcessoProc(models.Model):
    id_job_process = models.BigIntegerField()
    control = models.CharField(max_length=40, blank=True, null=True)
    procedure = models.CharField(max_length=255)
    date_initial = models.DateTimeField()
    date_final = models.DateTimeField(blank=True, null=True)
    status = models.BigIntegerField()
    message = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i902_processo_proc'


class I903ConcManual(models.Model):
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    id_manual = models.CharField(max_length=50, blank=True, null=True)
    tipo = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i903_conc_manual'


class I904DashboardValue(models.Model):
    id_dashboard_value = models.BigIntegerField(blank=True, null=True)
    id_tax = models.BigIntegerField(blank=True, null=True)
    priceaccount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    pricefiscal = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    linesaccount = models.BigIntegerField(blank=True, null=True)
    linesfiscal = models.BigIntegerField(blank=True, null=True)
    codconta = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i904_dashboard_value'


class I905FilterDashboard(models.Model):
    id_filter_dashboard = models.BigIntegerField(blank=True, null=True)
    id_company = models.BigIntegerField(blank=True, null=True)
    id_subsidiary = models.BigIntegerField(blank=True, null=True)
    id_category = models.BigIntegerField(blank=True, null=True)
    cod_account = models.CharField(max_length=70, blank=True, null=True)
    period = models.DateField(blank=True, null=True)
    control = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i905_filter_dashboard'


class I906FilterDashboardTax(models.Model):
    id_filter_dashboard_tax = models.BigIntegerField(blank=True, null=True)
    id_filter_dashboard = models.BigIntegerField(blank=True, null=True)
    id_tax = models.BigIntegerField(blank=True, null=True)
    control = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i906_filter_dashboard_tax'


class I907Layout(models.Model):
    id_layout = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    name_table = models.CharField(max_length=255, blank=True, null=True)
    enable = models.CharField(max_length=1, blank=True, null=True)
    control = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i907_layout'


class I908LayoutField(models.Model):
    id_layout_field = models.BigIntegerField(blank=True, null=True)
    id_layout = models.BigIntegerField(blank=True, null=True)
    field_source = models.CharField(max_length=255, blank=True, null=True)
    field_destiny = models.CharField(max_length=255, blank=True, null=True)
    field_order = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i908_layout_field'


class I909LayoutLog(models.Model):
    id_layout_log = models.BigIntegerField(blank=True, null=True)
    id_layout = models.BigIntegerField(blank=True, null=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_token = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField(blank=True, null=True)
    lines = models.BigIntegerField(blank=True, null=True)
    message = models.CharField(max_length=800, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'i909_layout_log'


class TbGrid(models.Model):
    ind_conciliado = models.CharField(max_length=10, blank=True, null=True)
    id_conciliacao = models.BigIntegerField(blank=True, null=True)
    id_empresa = models.BigIntegerField(blank=True, null=True)
    id_imposto = models.BigIntegerField(blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)
    id_filial_docto = models.FloatField(blank=True, null=True)
    num_docto = models.CharField(max_length=12, blank=True, null=True)
    data_docto = models.DateField(blank=True, null=True)
    vlr_docto = models.FloatField(blank=True, null=True)
    origem = models.CharField(max_length=4, blank=True, null=True)
    id_filial_lanc = models.FloatField(blank=True, null=True)
    num_lancto = models.CharField(max_length=60, blank=True, null=True)
    ind_deb_cred = models.CharField(max_length=1, blank=True, null=True)
    cod_conta = models.CharField(max_length=70, blank=True, null=True)
    vlr_lancto = models.FloatField(blank=True, null=True)
    data_lancto = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=14, blank=True, null=True)
    diferenca = models.FloatField(blank=True, null=True)
    data_operacao = models.DateField(blank=True, null=True)
    ind_nivel = models.CharField(max_length=1, blank=True, null=True)
    class_pendencia = models.CharField(max_length=255, blank=True, null=True)
    justificativa = models.CharField(max_length=255, blank=True, null=True)
    motivo = models.CharField(max_length=33, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_grid'
