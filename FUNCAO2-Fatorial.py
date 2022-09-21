def fatorial(num,show = True):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (Opicional) Mostrar ou não a conta.
        Desenvolvido por Devays.
    """

    f = 1
    if show == True:
        c = num
        while c > 0:
            print(f'{c} ',end='')
            print(' x ' if c > 1 else ' = ',end='') 
            f = f * c
            c = c - 1
        print(f)
    else:
        c = num
        while c > 0:
            f = f * c
            c = c - 1
        print(f)


fatorial(5,show=False)
