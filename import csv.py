import csv

fund_code = '000000'
operation_code = '300'


titulo_partida = {
    'PIX QRS CONSOLIDADO': 'C/C ITAU',
    'SISPAG DIVERSOS': 'C/C',
    'MOV TIT COB DISP': 'C/C ITAU',
    'TAR/CUSTAS COBRANCA': 'C/C ITAU',
}

titulo_contrapartida = {
    'TAR/CUSTAS COBRANCA': '#TAR.BANC',
    'PIX QRS CONSOLIDADO': 'DC.A.IDENTIF',
    'SISPAG DIVERSOS': 'C/C ITAU',
    'MOV TIT COB DISP': 'DC.A.IDENTIF',
}

historical = {
    'TAR/CUSTAS COBRANCA': 'Pagamento de tarifas bancarias',
    'PIX QRS CONSOLIDADO': 'PIX QRS CONSOLIDADO',
    'SISPAG DIVERSOS': 'Transferencia entre contas',
    'MOV TIT COB DISP': 'MOV TIT COB DISP',
}

# LER O ARQUIVO
# INCLUIR CODIGO DO FUNDO FIXO
# LER E INSERIR COLUNA DE DATA
# INCLUIR CODIGO DE OPERACAO (DEBITO/CREDITO) FIXO
# LER E INSERIR COLUNA DE VALOR
# DEFINIR TITULO PARTIDA COM BASE NO DICIONARIO
# DEFINIR TITULO CONTRAPARTIDA COM BASE NO DICIONARIO
# DEFINIR HISTORICO COM BASE NO DICIONARIO
# SALVAR ARQUIVO

arquivo_input = open('Extrato.txt','r')
arquivo_output = open('ExtratoExportado.txt','w')

linhas = csv.reader(arquivo_input, delimiter=";")

for linha in linhas:
    nova_linha = ''
    nova_linha += fund_code
    nova_linha += '             '
    nova_linha += linha[0] #DATA
    nova_linha += operation_code
    nova_linha += linha[2].replace('-','') #VALOR
    coluna1 = linha[1]
    if coluna1.startswith('MOV TIT COB DISP'):
        coluna1 = 'MOV TIT COB DISP'
    nova_linha += titulo_partida[coluna1]
    nova_linha += '             '
    nova_linha += titulo_contrapartida[coluna1]
    nova_linha += '             '
    nova_linha += historical[coluna1]
    print(nova_linha)

    arquivo_output.write(nova_linha + '\n')