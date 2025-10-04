import streamlit as st
import pandas as pd
from scraper.buscar import buscar_servicos
from ai.analisar import analisar_servico
import time

st.set_page_config(page_title="Serviços Freelance", layout="wide")
st.title("Análise de Serviços Freelance com Gemini AI")

page = st.number_input("Página", min_value=1, value=1)

st.write(f"Raspando dados da página {page}…")
servicos = buscar_servicos(page)

for servico in servicos:
    if servico.get("titulo") and servico.get("descricao"):
        servico["analise"] = analisar_servico(servico)
        time.sleep(30)

df = pd.DataFrame(servicos)

st.subheader("Serviços encontrados")
st.dataframe(df)

csv = df.to_csv(index=False, encoding="utf-8-sig")
st.download_button("Download CSV", data=csv, file_name="servicos_com_analise.csv", mime="text/csv")
