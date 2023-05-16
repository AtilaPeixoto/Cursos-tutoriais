from datetime import date
from time import sleep


cor = {"sublinhado": "\033[4m",
        "vermelho": "\033[31m",
       "negrito": "\033[1m",
       "branco": "\033[7m",
       "limpa": "\033[m"
       }


s = r = 0
saldoa = saldob = 0                                                                         # extrato
enfeite = "="*40                                                                            # enfeite
b = f"{cor['branco']}{cor['negrito']}{'BANCO':=^40}{cor['limpa']}"            # banco

saldo = float(3141592.63)                                                   # saldo inicial

print()
print(enfeite)
print(b)
print(enfeite)
print("                     INICIANDO")
sleep(3)


while True:
    m100 = 200
    print(f" {date.today()}       INSIRA O CARTAO")
    sleep(2)
    print()
    v = int(input("{} SENHA: {}".format(cor["negrito"], cor["limpa"])))      # senha negrito
    print(f"verificando", end=" ")                                           # pontos
    sleep(1)
    print(".", end=" ")
    sleep(1)
    print(".", end=" ")
    sleep(1)
    print(".", end=" ")
    print()
    
    
    for x in range(0, 3):
        n5 = n10 = n20 = n50 = n100 = 0                             # as notas
        print(enfeite)
        print(b)                                                   # banco
        print(date.today())
        print(f"{cor['negrito']} Seu SALDO R$: {saldo}{cor['limpa']} ")     # saldo na tela
        print(enfeite)
        print("Escolha uma opção;")          # menu principal
        funcao = input("""                              
        [1] Transferir
        [2] Sacar
        [3] Pagar
        [4] Extrato
        OPÇÃO: """)
        print(enfeite)
        
        
        if funcao == "1":
            print(enfeite)
            print(b)
            print(enfeite)
            print(f"""       Função indisponivel.\n             {cor['vermelho']} Sistema Fora de Rede{cor['limpa']}""")
            print(enfeite)
            
        elif funcao == "2":
            print(enfeite)
            print(b)
            print(enfeite)
            s = int(input("      Valor do Saque: "))    # Saque
            
            if s % 5 != 0:
                print(f"{cor['vermelho']}{cor['negrito']}PARA SAQUES PAENAS VALORES REDONDOS{cor['limpa']}")
                s = int(input("      Valor do Saque: "))
                
            saq = input("""
            [1] Escolher notas
            [2] Escolha automatica
            Sua opçao: """)
            
            if saq == "1":
                if s >= 100:
                    evn = input("""
                    [1] NOTAS DE R$100.00
                    [2] NOTAS DE R$50.00
                    [3] NOTAS DE R$20.00
                    [4] NOTAS DE R$10.00
                      """)
                    
                    if evn == "1":             # para valores maiores que cem no saque
                        r = s % 100
                        
                        if s >= 100:
                            n100 = s // 100
                        elif r >= 50:
                            n50 = r // 50
                            r = r % 50
                        elif r >= 20:
                            n20 = r // 20
                            r = r % 20
                        elif r >= 10:
                            n10 = r // 10
                            r = r % 10
                        elif r >= 5:
                            n5 = r // 5
                            
                            
                    elif evn == "2":           # opçao 2 escolher notas >100
                        n50 = s // 50
                        r = s % 50
                        n5 = r // 5
                    elif evn == "3":           # opçao 3 escolher notas >100
                        n20 = s // 20
                        r = s % 20
                        n5 = r // 5
                    elif evn == "4":          # opçao 4 escolher notas >100
                        n10 = s // 10
                        r = s % 10
                        n5 = r // 5


                elif 100 > s > 50:             # se menor que cem >50
                    evn = input("""
                    [1] NOTAS DE R$50.00
                    [2] NOTAS DE R$20.00
                    [3] NOTAS DE R$10.00
                        """)
                    
                    if evn == "1":             # opçao 1 escolher notas >50
                        n50 = s // 50
                        r = s % 50
                        n5 = r // 5
                    elif evn == "2":         # opçao 2 escolher notas >50
                        n20 = s // 20
                        r = s % 20
                        n5 = r // 5
                    elif evn == "3":        # opçao 3 escolher notas >50
                        n10 = s // 10
                        r = s % 10
                        n5 = r // 5
                        
                elif 50 > s > 20:          # para valores menores que cinquenta >20
                    evn = input("""
                     [1] NOTAS DE R$20.00
                     [2] NOTAS DE R$10.00
                            """)
                    
                    if evn == "1":       # opçao 1 escoher notas >20
                        r = s % 20
                        print(r)
                        n20 = s // 20
                        n5 = r // 5
                    elif evn == "2":       # opçao 2 escolher notas >20
                        n10 = s // 10
                        r = s % 10
                        n5 = r // 5
                        
                elif s < 20:               # para valores menores que vinte no saque < 20
                    evn = input(f"""
                    [1] NOTAS DE R$10.00
                    [{cor['vermelho']}X{cor['limpa']}]NOTAS DE R$5.00 {cor['limpa']}INDISPONIVEL{cor['limpa']}
                        """)
                    
                    if evn == "1":
                        n10 = s // 10
                        r = s % 10
                        n5 = r // 5
                        
                else:
                    print(f"{cor['vermelhor']} Valor muito baixo par saque{cor['limpa']}")
                    
                    
            else:
                r = s % 200                                 # aqui é o exerciocio o resto é extra
                if s >= 200:
                    n100 = s // 200
                if r >= 50:
                    n50 = r // 50
                    r = r % 50
                if r >= 20:
                    n20 = r // 20
                    r = r % 20
                if r >= 10:
                    n10 = r // 10
                    r = r % 10
                if r >= 5:
                    n5 = r // 5



            saldob = saldoa
            saldoa = saldo
            saldo -= s
            print(enfeite)
            print(enfeite)
            print(b)
            print(enfeite)
            print(date.today())
            print(f" Saque de {cor['negrito']}{s}{cor['limpa']}")
            print(f"{cor['negrito']}Novo SALDO: {saldo} {cor['limpa']}")
            print(f"Saldo anterior R${saldoa}")
            print(enfeite)
            
            if n100 > 0:
                print(f" total notas cem {n100}")
            if n50 > 0:
                print(f" total de notas cinquenta {n50}")
            if n20 > 0:
                print(f" total de notas vinte {n20}")
            if n10 > 0:
                print( f" total notas de dez {n10}")
            if n5 > 0:
                print(f" Total de notas  de cinco {n5}")
                
                
        elif funcao == "3":
            print(enfeite)
            print(b)
            print(enfeite)
            print(f"           Função indisponivel.\n        {cor['vermelho']} Sistema Fora de Rede{cor['limpa']}")
            print(enfeite)
        elif funcao == "4":
            print(f"""Transaçções recentes
            {cor['sublinhado']}{date.today()}{cor['limpa']}  {saldob}
            {cor['sublinhado']}{date.today()}{cor['limpa']}  {saldoa}
            {cor['sublinhado']}{date.today()}{cor['limpa']}  {cor['negrito']}Saldo atual:    {saldo}{cor['limpa']}
            """)
        else:
            print(enfeite)
            print(b)
            print(enfeite)
            print(f"         {cor['veermelho']}Opçao invalida{cor['limpa']}")
            print(enfeite)

    print(enfeite)
    print(b)
    print(enfeite)
    print("      Agradecemos sua preferencia.")         # agradecimento
    print(enfeite)
    print(b)                                           # logo para reinicio
    print(enfeite)
    break
