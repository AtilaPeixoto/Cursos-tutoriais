



v = int(input("qual velocidade que o veiculo esta? "))



if v>80:
    m = (v - 80)
    mul = m * 7
    print("O veiculo esta acima da velocidade em {}Km\nO valor a ser pago ao orgao de trasito como penalidade deve ser de R${:.2f}".format(m, mul))
else:
    print("parabens por ser um bom motoria.\n Parabens por ser um mtora responsa.")