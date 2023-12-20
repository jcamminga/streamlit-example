import streamlit as st
import pandas as pd
import random

# Functie om een willekeurige vraag en antwoord te kiezen
def select_random_question(df, question_column, answer_column):
    random_row = df.sample()
    question = random_row[question_column].values[0]
    answer = random_row[answer_column].values[0]
    return question, answer

# Functie om een dataframe te laden vanuit een Excel-bestand
def load_data(file_name, sheet_name=0):
    return pd.read_excel(file_name, sheet_name=sheet_name)

# Hoofdpagina setup
st.title("Quiz Applicatie")

# Pagina navigatie
page = st.sidebar.selectbox("Kies een pagina:", 
                            ["Champion titles", "Champion passives"])

# Pagina: Champion titles
if page == "Champion titles":
    df_titles = load_data("champion-title.xlsx")
    question, answer = select_random_question(df_titles, 'champ-list__item__title', 'champ-list__item__name')

    st.subheader("Champion Title Vraag")
    st.write(question)

    if st.button("Toon antwoord"):
        st.write(answer)

    if st.button("Nieuwe vraag"):
        st.experimental_rerun()

# Pagina: Champion passives
elif page == "Champion passives":
    df_passives = load_data("champion-abilities.xlsx")
    df_passives_filtered = df_passives[df_passives['ability-list__item__name'] == 'Passive']
    question, answer = select_random_question(df_passives_filtered, 'ability-list__item__name', 'combined')

    st.subheader("Champion Passive Vraag")
    st.write(question)

    if st.button("Toon antwoord"):
        st.write(answer)

    if st.button("Nieuwe vraag"):
        st.experimental_rerun()
