import streamlit as st 
import pandas as pd


st.set_page_config(page_title="Detalhes do livro",
                   page_icon="📚",
                   layout="wide")

df_books1 = df_top100_books = pd.read_csv("Datasets/Top-100 Trending Books.csv") #st.session_state["books"] # pego o que foi carregado na tela inicial
df_reviews = pd.read_csv("Datasets/customer reviews.csv")

books = df_books1["book title"].unique()
book = st.sidebar.selectbox("Livros", books)

df_reviews_f = df_reviews[df_reviews["book name"] == book]

df_books = df_books1[df_books1["book title"] == book]

titulo = df_books["book title"].iloc[0]
genero = df_books["genre"].iloc[0]
preco = f" ${df_books['book price'].iloc[0]}"
avaliacao = df_books["rating"].iloc[0]
publicacao = df_books["year of publication"].iloc[0]

st.title(titulo)
st.subheader(genero)

col1, col2, col3 = st.columns(3)

col1.metric("Preço", preco)
col2.metric("Avaliação", avaliacao)
col3.metric("Ano de Publicação", publicacao)

st.divider()

df_reviews_f

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}") 
    message.write(f"**{'Título Revisado: '}" + f"{row[2]}**")
    message.write(f"**{'Descrição da Revisão: '}**" + f" {row[5]}")
    st.divider()
