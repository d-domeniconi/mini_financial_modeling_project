# Mini Financial Modeling Project

Simulação de fluxo de caixa de uma operação de crédito indexada ao CDI com capitalização composta diária em base útil, incluindo calendário financeiro brasileiro, amortização mensal e visualizações analíticas.

---

## Objetivo

Este projeto implementa uma engine simplificada de modelagem financeira para projeção de passivos corporativos, seguindo regras típicas do mercado financeiro brasileiro.

O modelo considera:

- Capitalização composta diária;
- Incidência apenas em dias úteis;
- CDI diário + spread fixo;
- Calendário com feriados nacionais e estaduais;
- Pagamentos mensais no primeiro dia útil;
- Prioridade de pagamento de juros acumulados;
- Amortização do principal;
- Possibilidade de amortização negativa;
- Encerramento automático da dívida.

---

## Estrutura do Projeto

A organização do repositório reflete a separação entre módulos operacionais, exploração analítica e artefatos gerados:

```text
MINI_FINANCIAL_MODELING_PROJECT/
│
├── data/                                 # Outputs em Excel
│
├── figs/                                 # Gráficos e visualizações geradas
│
├── modules/
│   ├── amint.py                          # Lógica de amortização e juros
│   └── dina.py                           # Geração de dinâmica de capitalização
│
├── .gitignore
├── requirements.txt                      # Dependências do projeto
├── amortization_and_interest.ipynb       # Exploração do modelo de amortização
├── capitalization_dynamics.ipynb         # Análise do comportamento de juros
├── example.py                            # Script principal de execução
└── README.md
```

---

## Modelagem Financeira

### Fator de Atualização Diário

A cada dia útil:

```math
f_t = (1+i_{CDI}) \times (1+s_{fixa})
```

Onde:

- $\(i_{CDI}\)$: taxa CDI diária;
- $\(s_{fixa}\)$: spread fixo diário.

---

### Atualização do Saldo Devedor

```math
SD_t = SD_{t-1} \times f_t
```

---

### Juros do Dia

```math
J_t = SD_t - SD_{t-1}
```

---

### Regra de Pagamento

No primeiro dia útil de cada mês:

1. Os juros acumulados são quitados primeiro;
2. O restante da parcela amortiza o principal;
3. Caso os juros sejam maiores que a parcela:
   - ocorre amortização negativa;
   - o saldo devedor cresce.

---

## Funcionalidades

### Calendário Financeiro

A função:

```python
gerar_calendario_financeiro()
```

gera:

- dias úteis;
- fins de semana;
- feriados nacionais;
- feriados estaduais;
- datas de pagamento.

---

### Simulação de Fluxo de Caixa

A função:

```python
fluxo_de_caixa()
```

calcula diariamente:

- saldo inicial;
- juros do dia;
- juros acumulados;
- pagamento;
- amortização;
- saldo final.

---

### Relatório Mensal

A função:

```python
relatorio_mensal()
```

produz tabelas contendo:

- data do pagamento;
- juros acumulados;
- amortização;
- saldo remanescente.

---

### Visualizações

A função:

```python
visualizar_fluxo_de_caixa()
```

gera gráficos de:

- evolução do saldo devedor;
- composição dos pagamentos;
- acúmulo de juros.

Todos em escala de cinza para documentação técnica.

---

## Exemplo de Uso

```python
from modules.amint import (
    fluxo_de_caixa,
    visualizar_fluxo_de_caixa,
    relatorio_mensal,
    gerar_calendario_financeiro
)

# calendário financeiro
calendario = gerar_calendario_financeiro(
    inicio="2025-10-01",
    fim="2026-10-02",
    estado="SC"
)

# simulação
cash_flow = fluxo_de_caixa(
    aporte=3_000_000,
    t_cdi=0.05,
    s_fixa=0.02,
    parcela=150_000,
    calendario=calendario
)

# relatório
relatorio = relatorio_mensal(cash_flow)

print(relatorio)

# visualização
visualizar_fluxo_de_caixa(cash_flow)
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/d-domeniconi/mini_financial_modeling_project.git
```

Entre no diretório:

```bash
cd mini_financial_modeling_project
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Dependências

Principais bibliotecas utilizadas:

- pandas
- matplotlib
- seaborn
- holidays

---

## Convenções Financeiras

O projeto assume:

- Base útil 252;
- Capitalização composta;
- Incidência apenas em dias úteis;
- CDI diário constante por simplicidade.

---

## Possíveis Extensões

- Curva CDI histórica;
- Cenários estocásticos;
- Monte Carlo;
- Duration e convexidade;
- Stress testing;
- Dashboard interativo;
- Múltiplos contratos simultâneos.
