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
page = st.sidebar.selectbox("Kies een pagina:", ["Champion titles", "Champion passives"])

# Initialiseren of bijwerken van session_state variabelen
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = page
    st.session_state['question'] = ""
    st.session_state['answer'] = ""
    st.session_state['question_counter'] = 0

# Check voor paginawissel of nieuwe vraag
if page != st.session_state['current_page'] or st.session_state['question_counter'] != st.session_state.get('last_question_counter', 0):
    st.session_state['current_page'] = page
    st.session_state['last_question_counter'] = st.session_state['question_counter']

    if page == "Champion titles":
        df = load_data("champion-title.xlsx")
    elif page == "Champion passives":
        df = load_data("champion-abilities.xlsx")
        df = df[df['ability-list__item__keybind'] == 'Passive']
    st.session_state['question'], st.session_state['answer'] = select_random_question(df, 'champ-list__item__title', 'champ-list__item__name')

# Pagina inhoud
st.subheader(f"{page} Vraag")
st.write(st.session_state['question'])

if st.button("Toon antwoord"):
    st.write(st.session_state['answer'])

if st.button("Nieuwe vraag"):
    st.session_state['question_counter'] += 1
