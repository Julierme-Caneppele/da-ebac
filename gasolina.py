data = pd.read_csv('gasolina.csv')
df = pd.DataFrame(data)
gasolina = data[['dia', 'venda']].reset_index()
gasolina.head()
grafico = sns.barplot(data=gasolina, x='dia', y='venda', ci=None, palette='pastel')
grafico.set(title='Preço da gasolina', xlabel='Dia', ylabel= 'Venda');

import os

if not os.path.exists('gasolina.py'):
    os.makedirs('gasolina.py')

ax = grafico = sns.barplot(data=gasolina, x='dia', y='venda', ci=None, palette='pastel')
fig = ax.get_figure()
fig.savefig('preco_da_gasolina.png')