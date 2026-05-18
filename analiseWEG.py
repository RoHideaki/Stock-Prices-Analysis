import yfinance as yf
import matplotlib.pyplot as plt

#Baixando os dados do ticker com a biblio yf
ticker = 'VIVA3.SA'
acao = yf.download(ticker, start="2022-01-01")

#Mostra os preços
#print(acao.head())

#Gera o gráfico de preços
acao['Close'].plot(figsize=(10,5))

#Calculando o retorno acumulado
retorno = ((acao['Close'].iloc[-1] / acao['Close'].iloc[0]) - 1).item()
print(f'Retorno acumulado: {retorno:.2%}')

#Volatilidade anualizada
acao['Retorno_Diario'] = acao['Close'].pct_change()
volatilidade = acao['Retorno_Diario'].std() * (252 ** 0.5)
print(f'Volatilidade anualizada: {volatilidade:.2%}')

plt.title(f'Preço da {ticker}')
plt.show()

print('sucesso!')