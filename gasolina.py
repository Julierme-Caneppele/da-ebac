data = pd.read_csv('gasolina.csv')
df = pd.DataFrame(data)
gasolina = data[['dia', 'venda']].reset_index()
gasolina.head()
grafico = sns.barplot(data=gasolina, x='dia', y='venda', ci=None, palette='pastel')
grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel= 'Venda');