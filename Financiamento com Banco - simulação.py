#FINANCIANDO SEU IMÓVEL#

#ENTENDA QUE PRIMEIRO VOCÊ PAGA JUROS AO BANCO, DEPOIS A PARCELA DA SUA CASA PRÓPRIA#

valor_financiamento = int(input("Quanto você deseja financiar? "))
prazo = int(input("Determine um prazo para pagamento(20, 25 ou 30 anos)"))
taxa_de_juros = 0.009
print("A taxa de juros oferecida pelo nosso banco é de ",(taxa_de_juros*100),"% ao mês")
saldo_residual = valor_financiamento
mes = 0
while saldo_residual > 0:
    #ESSA SERÁ O VALOR MENSAL DE JUROS A SER ACRESCIDO NA PARCELA#
    mes += 1
    juros = saldo_residual*taxa_de_juros

    parcela_sem_juros = valor_financiamento/(prazo*12)
    parcela_com_juros = parcela_sem_juros + juros

    #O QUE O CLIENTE NÃO VE#
    #print("O valor mensal da 1ª parcela deveria ser de R$",parcela_sem_juros)#
    #print("O juros mensal do banco no 1º mês é de",juros)#

    #O QUE O CLIENTE NÃO VE#
    #print(parcela_com_juros)#

    #A cada mês de reduz apenas o valor da parcela sem juros#
    saldo_residual = saldo_residual - parcela_sem_juros
    
    print(f"O saldo do imóvel é de {saldo_residual:.2f}, a parcela total foi de R${parcela_com_juros:.2f} do {mes}º mês")


