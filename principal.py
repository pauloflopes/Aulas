import streamlit as st
import plotly.express  as px
import pandas as pd

st.set_page_config(page_title="Livros da Amazon Novembro/2023",
                   page_icon="📖",
                   layout="wide")

#if "books" not in st.session_state:
    
df_top100_books = pd.read_csv("Datasets/Top-100 Trending Books.csv")

 #   st.session_state["books"] = df_top100_books

preco_max = df_top100_books["book price"].max()
preco_min = df_top100_books["book price"].min()

preco_max = st.sidebar.slider("Preço", preco_min, preco_max, preco_max)
df_books = df_top100_books[df_top100_books["book price"] <= preco_max]

st.dataframe(df_books, column_config={
    "Rank": st.column_config.TextColumn(label="Posição"),
    "book title": st.column_config.TextColumn(label="Título"),
    "book price": st.column_config.TextColumn(label="Preço"),
    "rating": st.column_config.TextColumn(label="Avaliação"),
    "year of publication": st.column_config.TextColumn(label="Ano de Publicação"),
    "genre": st.column_config.TextColumn(label="Gênero"),
    }, height=300, width=1300
             )

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)


