n1 = float(input("Diga a primeira nota "))
n2 = float(input("Diga a segunda nota "))
m = (n1+ n2) / 2
if m >= 7:
    print("o aluno esta aprovado. \nCom nota {}".format(m))
elif m < 7 and m >= 5:
    print("O aluno esta em recuperaçao.\nCom nota {}".format(m))
else:
    m < 5
    print("O aluno foi reprovado. \nCom nota {} ".format(m))
