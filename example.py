from modules.amint import gerar_calendario_financeiro, fluxo_de_caixa, visualizar_fluxo_de_caixa
import matplotlib.pyplot as plt

# Parâmetros da Simulação:

aporte = 3e6 # reais

taxa_cdi = 0.05 # % por dia

taxa_fixa = 0.02 # % por dia

parcela_mensal = 150e3 # reais

data_inicio = "2025-10-1" # Data de Liberação
data_final = "2026-10-10" # Horizonte e simulação

regiao = "SC" # Santa Catarina


# Criar calendário:

calendario = gerar_calendario_financeiro(data_inicio, data_final, regiao)
print(calendario.head())


# Rodar simulação no tempo:

fluxo_no_periodo = fluxo_de_caixa(aporte,taxa_cdi,taxa_fixa,parcela_mensal,calendario)
print(fluxo_no_periodo.head())


# Plotar 
