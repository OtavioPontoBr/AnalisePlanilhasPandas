import openpyxl

#carregar arquivo exel

#PlanilhaClientes = openpyxl.load_workbook('vendas.xlsx')

#selecionando planilha

#Ler_Planilha = PlanilhaClientes['sheet1']

Clientes = ['Cliente 1', 'Cliente 2', 'Cliente 3', 'Cliente 4', 'Cliente 5', 'Cliente 6', 'Cliente 7'
, 'Cliente 8', 'Cliente 9', 'Cliente 10', 'Cliente 11', 'Cliente 12', 'Cliente 13', 'Cliente 14', 'Cliente 15'
, 'Cliente 16', 'Cliente 17', 'Cliente 18', 'Cliente 19', 'Cliente 20']

Numero_Vendas = 0
Valor_Vendido = 0

for cliente in Clientes:
    print(cliente)    
