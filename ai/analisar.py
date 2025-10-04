import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")
if GEMINI_KEY is None:
    raise ValueError("A variável GEMINI_KEY não foi encontrada no .env")
genai.configure(api_key=GEMINI_KEY)
modelo = genai.GenerativeModel("gemini-2.5-pro")

def analisar_servico(servico):
    prompt = f"""
    Analise o seguinte serviço freelance se ele se encaixos no que eu consigo trabalhar:
    - Excel
    - Power BI
    - Python (intermediário)
    - RPA (Robotic Process Automation)
    - SQL
    - Google Sheets
    - Google Data Studio
    - Google Cloud Platform (básico)
    - Power Point
    - Word
    - Qualquer banco de dados ou relacionado a dados
    Título: {servico['titulo']}
    Preço: {servico['preco']}
    Descrição: {servico['descricao']}
    Prazo: {servico['prazo']}
    Número de candidatos: {servico['candidatos']}

    Diga somente "Sim" se o serviço se encaixa nas minhas habilidades e "Não" caso contrário não fale nada além disso.
    """
    try:
        resposta = modelo.generate_content(prompt)
        return resposta.text
    except Exception as e:
        return f"Erro na análise: {e}"
