from datetime import date


hoje = date.today()
ano_atual = hoje.year
maior = 0
menor = 0

while True:

        ano_nasc = int(input("ano de nascimento: "))
        idade = (ano_atual - ano_nasc)

        if idade >= 18:
                maior = int(maior + 1)
        else:
                menor = int(menor +1)
                
        continuar = str(input('Adicionar mais um[S/N]: ')).lower()
        if continuar == 'n':
                break
        
        
print(f"São {maior} os maiores de idade")
print(f"São  {menor} os menores de idade")