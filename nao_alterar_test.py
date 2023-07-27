import exercicio1
import exercicio2


def test_caixa_eletronico():

    #caixa_eletronico
    assert exercicio1.caixa_eletronico(127) == (12,1,2)
    assert exercicio1.caixa_eletronico(145) == (14,1,0)


def test_eh_primo():

    #eh_primo
    assert exercicio2.eh_primo(10) == False
    assert exercicio2.eh_primo(7) == True
    assert exercicio2.eh_primo(15) == False