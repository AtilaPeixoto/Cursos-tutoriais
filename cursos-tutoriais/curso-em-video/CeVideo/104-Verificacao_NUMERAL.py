



def leiaInt(msg):
    ok = False
    valor = 0
    
    while True:
        n = str(input(msg))
        
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('erro')
            
        if ok:
            break
        
    return valor


n = leiaInt('numero')
print(f' voce digitou valor {n}')

