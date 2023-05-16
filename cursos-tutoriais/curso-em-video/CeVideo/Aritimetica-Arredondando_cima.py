# o modelo de cor4es ansi DE-ATE
# stylo - texto - fundo
# 0-7 * 30 - 37 * 40 - 47
from time import sleep
from math import ceil

# ceil -> arredonda para cima

cores = "\033[m red, \033[m green, \033[m white"

renda = float(input("Qual seu renda?"))

# o limite para emprestimo é 30% da renda
limite_para_emprestimo = renda * (30/100)

valor_desejado = float(input("qual valor do bem a ser adquirido?"))

numero_parcelas = int(input("Quantas parcelas ?"))

negar = "Sinto muito a solicitaçao foi negada.\nVou verifia oque posso fazer..."
analise = "Sua solicitaçao esta em analise..."
aprovado = "Parabens sua solicitaçao foi aprovada!\nEstará em 24hrs disponivel em sua conta."
resposta = "\nSerão um total de {} parcelas \nNo valor de R${}".format(numero_parcelas, (valor_desejado/numero_parcelas))

sleep(2)
print("Verificand Credito...")
sleep(2)
print("verificando Valor das parcelas...")
sleep(3)

if (valor_desejado / numero_parcelas) > limite_para_emprestimo:
    vp = negar
    print(vp)
    p2 = valor_desejado / limite_para_emprestimo
    print(f"""Ha uma oferta neste DISPONIVEL NESTE MODELO 
O total de parcelas entao é {ceil(p2)} \nO valor de cada Parcela é de R${limite_para_emprestimo:.2f} 
O valor total seria de R${ceil(p2) * limite_para_emprestimo:.2f}""")
else:
    print(aprovado, resposta)