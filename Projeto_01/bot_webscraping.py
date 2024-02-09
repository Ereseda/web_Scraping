print('Digite alguma skill que você não tenha como experiência: ')
excecao_skills = input('==>')
print(f'Removendo skill: {excecao_skills}')
import time
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.vagas.com.br/vagas-de-python?ordenar_por=mais_recentes').text
soup = BeautifulSoup(html_text, features= 'lxml')
vagas = soup.find_all('li', class_='vaga odd')
nome_arq = 0
total = 0
for campo in vagas:
    if("Hoje") or ("Ontem") or ("Há 3 dias") in campo.find('span', class_='data-publicacao').text.strip():
        nome_empresa = campo.find('span', class_='emprVaga').text.strip()
        nome_vaga = campo.find('h2', class_='cargo').text.strip()
        detalhe_vaga = campo.find('div', class_='detalhes').text.strip()
        if excecao_skills not in detalhe_vaga:
            nome_arq += 1
            with open(f'posts/{nome_arq}.txt', 'w') as arq_txt:
                arq_txt.write(f'Nome da Empresa: {nome_empresa.strip()}\n')
                arq_txt.write(f'Nome da Vaga: {nome_vaga.strip()}\n')
                arq_txt.write(f'Detalhes: {detalhe_vaga.strip()}\n')
            print(f'Arquivo{nome_arq} salvo.')