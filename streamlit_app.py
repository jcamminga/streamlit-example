import streamlit as st
import pandas as pd
import random

# Streamlit-applicatie
def main():
    st.title('Vragen en Antwoorden App')

    # Initialisatie van st.session_state
    if 'question' not in st.session_state:
        st.session_state.question = None
    if 'answer' not in st.session_state:
        st.session_state.answer = None
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    # Overzichtspagina met knoppen
    page = st.sidebar.selectbox('Selecteer een pagina:', ['Home', 'Vraag 1', 'Vraag 2', 'Vraag 3', 'Vraag 4', 'Vraag 5', 'Vraag 6'])

    if page == 'Home':
        st.header('Welkom op de overzichtspagina!')
        st.write('Kies een vraagcategorie hieronder:')

        # Knoppen voor verschillende vraagcategorieën
        if st.button('Vraag 1'):
            st.session_state.question, st.session_state.answer = get_random_question('champion-title.xlsx', 'champ-list__item__title', 'champ-list__item__name')
            st.session_state.show_answer = False
            page = 'Vraag 1'  # Schakel automatisch naar de Vraag 1-pagina

        if st.button('Vraag 2'):
            st.session_state.question, st.session_state.answer = get_random_question('champion-abilities.xlsx', 'ability-list__item__name', 'combined')
            st.session_state.show_answer = False
            page = 'Vraag 2'  # Schakel automatisch naar de Vraag 2-pagina

        # Voeg hier de knoppen voor Vraag 3 tot Vraag 6 toe op dezelfde manier

    elif page.startswith('Vraag'):
        st.header(page)
        st.write('Vraag: ' + st.session_state.question)

        # Knop om antwoord te tonen
        if st.button('Toon antwoord'):
            st.write('Antwoord: ' + st.session_state.answer)
            st.session_state.show_answer = True

        # Knop om terug te gaan naar overzichtspagina
        if st.button('Terug'):
            st.session_state.question, st.session_state.answer = None, None
            st.session_state.show_answer = False
            page = 'Home'  # Schakel automatisch naar de Home-pagina

    if st.session_state.show_answer and page.startswith('Vraag'):
        st.write('Antwoord: ' + st.session_state.answer)

    if page != 'Home':
        # Laat een knop zien om opnieuw de Vraag-pagina te openen voor nieuwe vragen
        if st.button('Opnieuw Vraag'):
            if page == 'Vraag 1':
                st.session_state.question, st.session_state.answer = get_random_question('champion-title.xlsx', 'champ-list__item__title', 'champ-list__item__name')
            elif page == 'Vraag 2':
                st.session_state.question, st.session_state.answer = get_random_question('champion-abilities.xlsx', 'ability-list__item__name', 'combined')
            st.session_state.show_answer = False

if __name__ == '__main__':
    main()
