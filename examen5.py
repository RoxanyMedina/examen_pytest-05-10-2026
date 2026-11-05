# def quadro(x):
#     return x * x

def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError('divisor zero')