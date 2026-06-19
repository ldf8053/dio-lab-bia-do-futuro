import json
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os
from google import genai

base_dir = os.path.dirname(os.path.abspath(__file__))

# configuracao
dotenv_path = os.path.join(base_dir, ".env")

# força a sobrescrever variáveis já existentes
load_dotenv(dotenv_path, override=True)
API_KEY = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

# Carregar dados

perfil_path = os.path.join(base_dir, '..', 'data', 'perfil_usuario.json')
transacoes_path = os.path.join(base_dir, '..', 'data', 'transacoes.csv')
produtos_path = os.path.join(base_dir, '..', 'data', 'produtos_saude.json')

with open(perfil_path, 'r', encoding='utf-8') as f:
    perfil = json.load(f)

transacoes = pd.read_csv(transacoes_path)

with open(produtos_path, 'r', encoding='utf-8') as f:
    produtos = json.load(f)


# Montar contexto
contexto = f"""
USUARIO: nome {perfil['nome']}, {perfil['idade']} anos, profissão {perfil['profissao']}
OBJETIVO: {perfil['objetivo_principal']}
CUSTOS INICIAIS: R$ {perfil['custos_farmacia_inicial']}

TRANSACOES RECENTES:
{transacoes.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# System prompt
SYSTEM_PROMPT = """Você é a Mari, um educador financeiro em saúde.

Seu objetivo principal é educar de forma amigável sobre produtos/serviços em saúde.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos para dar exemplos personalizados.
2. Nunca invente custos de serviços.
3. Use uma linguagem simples, como se estivesse falando com um amigo.
3. Se não souber algo, admita que não tem essa informação e ofereça alternativas como "mas posso explicar..."
5. Nunca recomende tratamentos medicamentosos, treinos físicos ou esportes, ou terapia de forma específica, apenas apresente quais opções estão disponíveis.
6. Sempre recomende acompanhamento de profissional de saúde para prática do serviço sugerido.
"""


# chamar LLM (Google Studio AI) 
def perguntar (msg):
    prompt = f"""
{SYSTEM_PROMPT}

INFORMACOES DO USUARIO:
{contexto}

PERGUNTA DO USUARIO:
{msg}
"""
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Desculpe, ocorreu um erro ao consultar a IA:\n\n{e}"


# interface
st.title(" \U0001F4AA Mari, sua educadora financeira em saúde")

if pergunta := st.chat_input("Sua dúvida sobre seus investimentos em saúde..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("Mari está pensando..."):
        response = perguntar(pergunta)

    st.chat_message("assistant").write(response)


