import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.vintepila.com.br/trabalhos-freelance/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/58.0.3029.110 Safari/537.3'
}

def buscar_servicos(page):
    url = f'{BASE_URL}?page={page}'
    response = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    blocks = soup.find_all('div', class_='content')
    
    servicos = []
    for block in blocks:
        titulo_elem = block.find('a', class_='header')
        titulo = titulo_elem.get_text(strip=True) if titulo_elem else None
        link = titulo_elem['href'] if titulo_elem and titulo_elem.has_attr('href') else None

        preco_elem = block.find('span', id='project-price')
        preco = preco_elem.get_text(strip=True) if preco_elem else None

        desc_elem = block.find('div', class_='description')
        descricao = desc_elem.get_text(strip=True) if desc_elem else None

        extra_spans = block.find('div', class_='extra').find_all('span') if block.find('div', class_='extra') else []
        publicado = extra_spans[0].get_text(strip=True) if len(extra_spans) > 0 else None
        prazo = extra_spans[1].get_text(strip=True) if len(extra_spans) > 1 else None
        candidatos = extra_spans[2].get_text(strip=True) if len(extra_spans) > 2 else None

        servico = {
            "titulo": titulo,
            "descricao": descricao,
            "preco": preco,
            "publicado": publicado,
            "prazo": prazo,
            "candidatos": candidatos,
            "link": link
        }

        # Só adiciona se nenhum valor for None
        if all(v is not None for v in servico.values()):
            servicos.append(servico)

    return servicos
