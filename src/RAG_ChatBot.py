import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate

st.title("ERM Tutor AI")
st.write("✅ This demo app is ready to deploy with all fixed dependencies.")
