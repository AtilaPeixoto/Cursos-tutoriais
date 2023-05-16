


cont = barato = caros = total = 0
c = ""


while True:
    pro = str(input("Item: ")).upper().strip()
    preço = int(input("valor R$: "))
    add = str(input("\033[1mAdd[S/N]\033[m ")).lower()
    total +=  preço
    
    if cont == 0:
        barato = preço
        baraton = pro
        
    elif barato > preço:
        barato = preço
        baroton = pro
        
    if preço > 500:
        caros += 1
        c = f" Haviam {caros} produtos acima de 500"
        
        
    cont += 1
    if add == "n":
        break
    
print(f"""
O total de produtos foi {cont}
O total gasto foi {total:.2f}
O produto mais barato foi {baraton}
{c}""")