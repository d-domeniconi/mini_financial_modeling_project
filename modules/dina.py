# capitalization_dynamics's module. This module contains functions related to the dynamics of capitalization in financial markets.

def fator_atualizacao(i_cdi, s_fixa, dia_util=True):
    """
    Calcula o fator diário de atualização de um saldo devedor.

    - `i_cdi` é a taxa diária do CDI em porcentagem;
    - `s_fixa` é o spread fixo diário em porcentagem.

    Em dias não úteis, o fator de atualização é igual a 1.

    Parameters
    ----------
    i_cdi : float
        Taxa diária do CDI (%).

    s_fixa : float
        Spread fixo diário (%).

    dia_util : bool, optional
        Indica se o dia é útil. Default é True.

    Returns
    -------
    float
        Fator diário de atualização do saldo devedor.
    """
    if dia_util:
        return (1 + i_cdi/100) * (1 + s_fixa/100)
    else:
        return 1
    
def saldo_devedor_atual(saldo_anterior, fator):
    """
    Calcula o saldo devedor atualizado para o período atual.

    O cálculo é realizado multiplicando o saldo devedor do período
    anterior pelo fator de atualização correspondente.

    Parameters
    ----------
    saldo_anterior : float
        Saldo devedor do período anterior.

    fator : float
        Fator de atualização aplicado ao saldo.

    Returns
    -------
    float
        Saldo devedor atualizado.
    """
    return saldo_anterior * fator

def juro_do_dia(saldo_atual, saldo_anterior):
    """
    Calcula o juro acumulado no dia.

    O valor é obtido pela diferença entre o saldo devedor atualizado
    e o saldo devedor do período anterior.

    Parameters
    ----------
    saldo_atual : float
        Saldo devedor atualizado.

    saldo_anterior : float
        Saldo devedor do período anterior.

    Returns
    -------
    float
        Valor do juro acumulado no dia.
    """
    return saldo_atual - saldo_anterior