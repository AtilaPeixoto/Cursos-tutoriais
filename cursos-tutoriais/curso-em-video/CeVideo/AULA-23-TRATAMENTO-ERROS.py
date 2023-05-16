try:
    n = int(input('NUMERO: '))
    n2 = int(input(' divisor: '))
    x = n / n2
    print(f' a resposta é {x}')
except (ValueError, TypeError):
    print(f' tivemos um problema com os tipos de dados')
except ZeroDivisionError:
    print('numero nao pode ser dividido por zero')
except KeyboardInterrupt:
    print(f' o usuario nao informou os dados')
except Exception as erro:
    print(f'o erro encontrado foi {erro.__class__}')
#except Exception as erro:
#    print(f' o erro encontrado foi {erro.__cause__}')
#except Exception as erro:
#    print(f' o erro encontrado foi {erro.__context__}')
else:
    print(f'o resultado é {x:.2f}')
finally:
    print('Volte sempre!!!')
