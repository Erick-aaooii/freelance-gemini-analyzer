# Análise de Serviços Freelance com Gemini AI

Este projeto permite raspar serviços freelance de um site, analisar se eles se encaixam nas suas habilidades e gerar um relatório em CSV utilizando a **API Gemini AI**.

---

## Funcionalidades

- Raspagem de serviços freelance da página selecionada do [VintePila](https://www.vintepila.com.br/).  
- Filtragem automática de serviços que tenham **todos os campos preenchidos**.  
- Análise automática de cada serviço utilizando **Gemini AI**, verificando se se encaixa nas suas habilidades.  
- Exportação dos resultados para **CSV**.  
- Integração com **Streamlit** para interface web interativa.

---

## Requisitos

- Python 3.10 ou superior
- Bibliotecas Python:
  - `requests`
  - `beautifulsoup4`
  - `pandas`
  - `streamlit`
  - `python-dotenv`
  - `google-generativeai`  

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

1. Crie um arquivo .env dentro da pasta "ai" e crie a variavel GEMINI_KEY que terá o valor da sua Chave API do gemini.

```bash
GEMINI_KEY="SUA_CHAVE_DA_API_GEMINI"
```

## Estrutura de pastas
```markdown
vintepilaapi/
├─ app.py
├─ scraper/
│  ├─ __init__.py
│  └─ buscar.py
├─ ai/
│  ├─ __init__.py
│  └─ analisar.py
├─ .env
└─ requirements.txt
```

## Uso
Rodando a interface web
```bash
streamlit run app.py
```

- Escolha a página de serviços que deseja raspar.
- Aguarde enquanto cada serviço é analisado pela Gemini AI (recomendado 30s de intervalo para evitar exceder o limite de requisições da API).
- Baixe os resultados em CSV.

## Tecnologias
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) 
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Google Gemini](https://ai.google/?utm_source=ai-google-com&utm_medium=redirect&utm_campaign=ai-google-com-website-redirect)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Licença
Este projeto está sob a licença MIT.