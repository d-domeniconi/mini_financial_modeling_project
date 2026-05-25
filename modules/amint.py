import holidays
import pandas as pd

def gerar_calendario_financeiro(inicio: str, fim: str, estado: str = "SC") -> pd.DataFrame:
    """
    Gera um calendário financeiro diário com identificação de dias úteis,
    fins de semana, feriados e eventos de pagamento.

    O calendário é construído para o intervalo [inicio, fim] e inclui
    marcações úteis para aplicações financeiras, como definição do primeiro
    dia útil de cada mês como data de pagamento.

    Parameters
    ----------
    inicio : str
        Data inicial do período no formato reconhecido pelo pandas (ex: 'YYYY-MM-DD').
    fim : str
        Data final do período no formato reconhecido pelo pandas (ex: 'YYYY-MM-DD').
    estado : str, default "SC"
        Subdivisão do Brasil usada para cálculo de feriados estaduais (ex: 'SP', 'RJ', 'SC').

    Returns
    -------
    pd.DataFrame
        DataFrame contendo as seguintes colunas:
        
        - data : datetime64[ns]
            Sequência diária do período solicitado.
        - dia_semana_num : int
            Dia da semana (0=segunda-feira, 6=domingo).
        - dia_semana : str
            Nome do dia da semana.
        - fim_de_semana : bool
            Indica se a data é sábado ou domingo.
        - feriado : object
            Nome do feriado (quando aplicável), caso contrário NaN.
        - eh_feriado : bool
            Indica se a data é feriado nacional ou estadual.
        - dia_util : bool
            Indica se a data é dia útil (não fim de semana e não feriado).
        - eh_pagamento : bool
            Marca o primeiro dia útil de cada mês como data de pagamento.

    Notes
    -----
    - Os feriados são obtidos via `holidays.Brazil`.
    - A definição de "dia útil" considera apenas fim de semana e feriados,
      sem ajustes de mercado financeiro (ex: feriados bancários específicos).
    - O critério de pagamento assume o primeiro dia útil de cada mês.

    Examples
    --------
    >>> df = gerar_calendario_financeiro("2024-01-01", "2024-03-31", estado="SC")
    >>> df[df["eh_pagamento"]][["data"]]
    """

    # get dates
    datas = pd.date_range(start=inicio, end=fim, freq="D")
    df = pd.DataFrame({"data": datas})

    # get weedays
    df["dia_semana_num"] = df["data"].dt.weekday
    df["dia_semana"] = df["data"].dt.day_name()
    df["fim_de_semana"] = df["dia_semana_num"] >= 5

    # get holidays
    anos_no_periodo = list(range(datas.min().year, datas.max().year + 1))
    feriados_br = holidays.Brazil(subdiv=estado, years=anos_no_periodo)
    df["feriado"] = df["data"].dt.date.map(feriados_br)
    df["eh_feriado"] = df["feriado"].notna()

    # indendificar dias úteis
    df["dia_util"] = ~df["fim_de_semana"] & ~df["eh_feriado"]

    # marcar o primeiro dia útil de cada mês
    df["eh_pagamento"] = False
    idx_pagamentos = (
        df[df["dia_util"]]
        .groupby(df["data"].dt.to_period("M"))
        .head(1)
        .index)
    df.loc[idx_pagamentos, "eh_pagamento"] = True

    return df