s = int(input("valor o saque"))
total = s
cedulas = 50  # valor da cedula
totcedula = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totcedula += 1
    else:
        print(f"total de {totcedula} cedulas de {cedulas}")
        if cedulas == 50:
             cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 5
        totcedula = 0
        if total == 0:
            break




