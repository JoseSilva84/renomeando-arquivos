import os

pasta = r'C:\Users\curso\Downloads\Python\leitor de objetos\renomeando'
formato = 'jpg'
compondo_formato = f'.{formato}'
arquivos_total = [f for f in os.listdir(pasta) if f.lower().endswith(compondo_formato)]
cada_arquivo = [f for f in os.listdir(pasta)]
qtde_jpg = len(arquivos_total)
print(f'Quantidade de arquivos em jpg: {qtde_jpg}')
print(cada_arquivo)
# print(os.getcwd())

cont = 1
for arquivo in arquivos_total:
    if arquivo != f'1.{formato}':
        cont += 1
        os.rename(arquivo, f'{cont}.{formato}')