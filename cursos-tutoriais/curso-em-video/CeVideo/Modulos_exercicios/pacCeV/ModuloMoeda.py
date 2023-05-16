


def resumo():
    """
    bla bla
    :return:
    """


def dobro(x=0, des=False):
    x = float(x)
    x *= 2
    if des:
        x = moeda(x)
    return x


def metade(x=0, des=False):
    x = float(x)
    x /= 2
    if des:
        x = moeda(x)
    return x


def aumentar(x=0, des=False):
    x = float(x)
    x += 20 * (x / 100)
    if des:
        x = moeda(x)
    return x


def diminuir(x=0, des=False):
    x = float(x)
    x -= 10 * (x / 100)
    if des:
        x = moeda(x)
    return x


def moeda(x, des=True):
    x = float(x)
    if des:
        f = f'{"R$ "}{x:.2f}'.replace('.', ',')
    else:
        f = x
    return f

