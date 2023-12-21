import streamlit as st
import pandas as pd
import random

# Functie om een willekeurige vraag en antwoord te kiezen
def select_random_question(df, question_column, answer_column):
    random_row = df.sample()
    question = random_row[question_column].values[0]
    answer = random_row[answer_column].values[0]
    return question, answer

# Functie om een willekeurige vraag en antwoord te kiezen
def select_random_question_detailed(df, question_column, answer_column, caption_column):
    random_row = df.sample()
    question = random_row[question_column].values[0]
    answer = random_row[answer_column].values[0]
    caption = random_row[caption_column].values[0]
    return question, answer, caption

# Functie om een dataframe te laden vanuit een Excel-bestand
def load_data(file_name, sheet_name=0):
    return pd.read_excel(file_name, sheet_name=sheet_name)

# Hoofdpagina setup
st.title("Trivia Legends")
st.subheader('A league of legends Trivia game', divider='red')

# Pagina navigatie
selected_page = st.sidebar.selectbox("Kies een pagina:", ["Champion titles", "Champion passives", "Champion abilities"', "Runes", "Item costs"])

# Controleer of de pagina is gewijzigd
if 'current_page' not in st.session_state or st.session_state['current_page'] != selected_page:
    st.session_state['current_page'] = selected_page
    st.session_state['load_new_question'] = True

# Initialiseren van session_state variabelen
if 'question' not in st.session_state or 'answer' not in st.session_state:
    st.session_state['question'] = ""
    st.session_state['answer'] = ""

# Pagina: Champion titles
if selected_page == "Champion titles":
    df_titles = load_data("champion-title.xlsx")

    if st.session_state.get('load_new_question', False):
        st.session_state['question'], st.session_state['answer'] = select_random_question(df_titles, 'champ-list__item__title', 'champ-list__item__name')
        st.session_state['load_new_question'] = False  # Reset de vlag na het laden van de nieuwe vraag

    st.subheader("Van welke champion is dit de titel:")
    st.write(st.session_state['question'])

    if st.button("Toon antwoord"):
        st.write(st.session_state['answer'])

    # Knop 'Nieuwe vraag' - zet de vlag voor het laden van een nieuwe vraag
    if st.button("Nieuwe vraag"):
        st.session_state['load_new_question'] = True
        st.rerun()  # Herlaad de pagina om de nieuwe vraag te tonen

# Pagina: Champion passives
elif selected_page == "Champion passives":
    df_passives = load_data("champion-abilities.xlsx")
    df_passives_filtered = df_passives[df_passives['ability-list__item__keybind'] == 'Passive']

    if st.session_state.get('load_new_question', False):
        st.session_state['question'], st.session_state['answer'] = select_random_question(df_passives_filtered, 'ability-list__item__name', 'combined')
        st.session_state['load_new_question'] = False  # Reset de vlag na het laden van de nieuwe vraag

    st.subheader("Van welke champion is dit de passive:")
    st.write(st.session_state['question'])

    if st.button("Toon antwoord"):
        st.write(st.session_state['answer'])

    # Knop 'Nieuwe vraag' - zet de vlag voor het laden van een nieuwe vraag
    if st.button("Nieuwe vraag"):
        st.session_state['load_new_question'] = True
        st.rerun()  # Herlaad de pagina om de nieuwe vraag te tonen

# Pagina: Champion abilities
elif selected_page == "Champion abilities":
    df_abilities = load_data("champion-abilities.xlsx")
    df_abilities_filtered = df_abilities[df_abilities['ability-list__item__keybind'] != 'Passive']

    if st.session_state.get('load_new_question', False):
        st.session_state['question'], st.session_state['answer'] = select_random_question(df_abilities_filtered, 'full image', 'combined')
        st.session_state['load_new_question'] = False  # Reset de vlag na het laden van de nieuwe vraag

    st.subheader("Welke ability is dit?:")
    st.image(st.session_state['question'], width=200)

    if st.button("Toon antwoord"):
        st.write(st.session_state['answer'])

    # Knop 'Nieuwe vraag' - zet de vlag voor het laden van een nieuwe vraag
    if st.button("Nieuwe vraag"):
        st.session_state['load_new_question'] = True
        st.rerun()  # Herlaad de pagina om de nieuwe vraag te tonen

# Pagina: Runes
elif selected_page == "Runes":
    df_runes = load_data("runes.xlsx")

    if st.session_state.get('load_new_question', False):
        st.session_state['question'], st.session_state['answer'] = select_random_question(df_runes, 'full image', 'Rune')
        st.session_state['load_new_question'] = False  # Reset de vlag na het laden van de nieuwe vraag

    st.subheader("Welke rune is dit?:")
    st.image(st.session_state['question'], width=200)

    if st.button("Toon antwoord"):
        st.write(st.session_state['answer'])

    # Knop 'Nieuwe vraag' - zet de vlag voor het laden van een nieuwe vraag
    if st.button("Nieuwe vraag"):
        st.session_state['load_new_question'] = True
        st.rerun()  # Herlaad de pagina om de nieuwe vraag te tonen

# Pagina: Item costs
elif selected_page == "Item costs":
    df_items = load_data("Items.xlsx")
    df_items_filtered = df_items[df_items['Cost'] < 2000]

    if st.session_state.get('load_new_question', False):
        st.session_state['question'], st.session_state['answer'], st.session_state['caption'] = select_random_question_detailed(df_items_filtered, 'Image', 'Cost', 'Item')
        st.session_state['load_new_question'] = False  # Reset de vlag na het laden van de nieuwe vraag

    st.subheader("Welke rune is dit?:")
    st.image(st.session_state['question'], width=200, caption = st.session_state['caption'] )

    if st.button("Toon antwoord"):
        st.write(st.session_state['answer'])

    # Knop 'Nieuwe vraag' - zet de vlag voor het laden van een nieuwe vraag
    if st.button("Nieuwe vraag"):
        st.session_state['load_new_question'] = True
        st.rerun()  # Herlaad de pagina om de nieuwe vraag te tonen
