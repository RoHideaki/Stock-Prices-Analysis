import yfinance as yf
import matplotlib.pyplot as plt

#Baixando os dados do ticker com a biblio yf
ticker = 'WEGE3.SA'
acao = yf.download(ticker, start="2022-01-01")
ibov = yf.download('^BVSP', start="2022-01-01")

#Mostra os preços
#print(acao.head())
#print(ibov.head())

#Gera o gráfico de preços
acao['Close'].plot(figsize=(10,5))

#Calculando o retorno acumulado
retorno = ((acao['Close'].iloc[-1] / acao['Close'].iloc[0]) - 1).item()
retorno_ibov = ((ibov['Close'].iloc[-1] / ibov['Close'].iloc[0]) - 1).item()

print(f'Retorno acumulado: {retorno:.2%}')
print(f'Retorno do IBOV: {retorno_ibov:.2%}')

#Volatilidade anualizada
acao['Retorno_Diario'] = acao['Close'].pct_change()
volatilidade = acao['Retorno_Diario'].std() * (252 ** 0.5)
ibov['Retorno_Diario'] = ibov['Close'].pct_change()
volatilidade_ibov = ibov['Retorno_Diario'].std() * (252 ** 0.5)

print(f'Volatilidade anualizada: {volatilidade:.2%}')
print(f'Volatilidade do IBOV: {volatilidade_ibov:.2%}')

acao_normalizada = acao['Close'] / acao['Close'].iloc[0] * 100
ibov_normalizado = ibov['Close'] / ibov['Close'].iloc[0] * 100

plt.figure(figsize=(12,6))
plt.plot(acao_normalizada, label=ticker)
plt.plot(ibov_normalizado, label='IBOV')
plt.legend()

plt.title(f'Preço da {ticker}')
plt.show()

print('sucesso!')