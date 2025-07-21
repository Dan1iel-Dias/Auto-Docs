import streamlit as st
from mentor import obter_situacao_resultado_com_login
from gerador_doc import gerar_comprovante
from documentos import buscar_documentos_aluno
import os

st.set_page_config(page_title="Consulta Escolar CEAP")

# Usuários autorizados e suas senhas do Mentor
usuarios_autorizados = {
    "Daniel": {"senha": "5673D15d@", "mentor_user": "daniel.santos@pedreira.org", "mentor_pass": "5673D15d@"},
    "Simone": {"senha": "12345", "mentor_user": "simone@pedreira.org", "mentor_pass": "12345"},
    "joao": {"senha": "senha3", "mentor_user": "joao@pedreira.org", "mentor_pass": "senha3"},
    "ana": {"senha": "senha4", "mentor_user": "ana@pedreira.org", "mentor_pass": "senha4"}
}

if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

if not st.session_state.autenticado:
    st.title("🔒 Login - Secretaria")  # Título só aparece na tela de login
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    if st.button("Entrar"):
        if usuario in usuarios_autorizados and senha == usuarios_autorizados[usuario]["senha"]:
            st.session_state.autenticado = True
            st.session_state.usuario = usuario
            st.success("✅ Login realizado com sucesso!")
            st.rerun()
        else:
            st.error("❌ Usuário ou senha inválidos.")
    st.stop()

# Interface principal após login
st.title("🔍 Automações - Secretaria")
st.write(f"Bem-vindo, **{st.session_state.usuario}**!")

nome = st.text_input("Digite o nome do aluno")
fase = st.selectbox("Qual fase o aluno pertence?", ["", "ECI", "EPT"])
modelo_input = st.text_input("Digite o nome do modelo (ex: declaracao_de_contraturno)")

if st.button("Consultar"):
    if not nome or not fase or not modelo_input:
        st.warning("⚠️ Preencha todos os campos!")
    else:
        usuario_mentor = usuarios_autorizados[st.session_state.usuario]["mentor_user"]
        senha_mentor = usuarios_autorizados[st.session_state.usuario]["mentor_pass"]

        try:
            dados = obter_situacao_resultado_com_login(nome, usuario_mentor, senha_mentor, fase)
            documentos = buscar_documentos_aluno(nome, usuario_mentor, senha_mentor)
            caminho_arquivo = gerar_comprovante(
                dados,
                nome,
                modelo_input,
                documentos_extra=documentos,
                fase=fase
            )

            st.success("✅ Documento gerado com sucesso!")

            st.write(f"📘 **Curso**: {dados.get('curso', '')}")
            for f in dados["fases"]:
                st.write(f"• Período: {f['periodo_letivo']} | Fase: {f['fase']} | Situação: {f['situacao_resultado']}")

            with open(caminho_arquivo, "rb") as file:
                st.download_button(
                    label="📄 Baixar Comprovante",
                    data=file,
                    file_name=os.path.basename(caminho_arquivo),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        except Exception as e:
            st.error(f"❌ Erro: {e}")