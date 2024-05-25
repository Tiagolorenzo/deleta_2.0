# usuario informa diretamente o nome que quer ser deletado
# lista
cidades = ['gama', 'taguatinga', 'sobradinho', 'sudoeste']

# usuario informa
cidade_deletada = input('Informe a cidade que quer deletar: ')

# deleta cidade informada
try:
    cidades.remove(cidade_deletada)
except:
    print('Não foi possível remover a cidade.')

# exibe a lista na tela
for cidade in cidades:
    print(cidade)
    