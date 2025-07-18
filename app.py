import streamlit as st
from mentor import obter_situacao_resultado_com_login
from gerador_doc import gerar_comprovante
from documentos import buscar_documentos_aluno
import os

st.set_page_config(page_title="Consulta Escolar CEAP")

st.title("🔍 Consulta Situação Escolar - CEAP")

# Inputs
nome = st.text_input("Digite o nome do aluno")
fase = st.selectbox("Qual fase o aluno pertence?", ["", "ECI", "EPT"])
modelo_input = st.text_input("Digite o nome do modelo (ex: declaracao_de_contraturno)")

# Botão de envio
if st.button("Consultar"):
    if not nome or not fase or not modelo_input:
        st.warning("⚠️ Preencha todos os campos!")
    else:
        usuario = "daniel.santos@pedreira.org"
        senha = "5673D15d@"

        try:
            dados = obter_situacao_resultado_com_login(nome, usuario, senha, fase)
            documentos = buscar_documentos_aluno(nome, usuario, senha)
            caminho_arquivo = gerar_comprovante(
                dados,
                nome,
                modelo_input,
                documentos_extra=documentos,
                fase=fase
            )

            st.success("✅ Documento gerado com sucesso!")

            # Mostrar resultados
            st.write(f"📘 **Curso**: {dados.get('curso', '')}")
            for f in dados["fases"]:
                st.write(f"• Período: {f['periodo_letivo']} | Fase: {f['fase']} | Situação: {f['situacao_resultado']}")

            # Botão de download
            with open(caminho_arquivo, "rb") as file:
                st.download_button(
                    label="📄 Baixar Comprovante",
                    data=file,
                    file_name=os.path.basename(caminho_arquivo),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                )
        except Exception as e:
            st.error(f"❌ Erro: {e}")
