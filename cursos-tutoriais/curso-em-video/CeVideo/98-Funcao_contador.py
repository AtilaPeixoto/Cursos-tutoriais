from time import sleep


def cont(a, b, c):
    if c < 0:
        
        while a > b:
            a += c
            print(f'{a} ->', end=' ', flush=True)
            sleep(.5)
        print('FIM')
        
    elif a < b:
        while a < b:
            a += c
            print(f'{a} ->', end=' ', flush=True)
            sleep(.5)
        print('FIM')
        
    elif a > b:
        c = -c
        
        while a > b:
            a += c
            print(f'{a} ->', end=' ', flush=True)
            sleep(0.5)
        print('FIM')

i = int(input('INICIO'))
f = int(input('FINAL'))
s = int(input('SALTO'))
cont(i, f, s)
