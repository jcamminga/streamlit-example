import streamlit as st
import pandas as pd

def get_random_question(excel_file_path, question_column, answer_column):
    df = pd.read_excel(excel_file_path)
    random_row = df.sample(1)
    question = random_row[question_column].values[0]
    answer = random_row[answer_column].values[0]
    return question, answer

def set_question_and_answer(category):
    if category == 'Vraag 1':
        return get_random_question('champion-title.xlsx', 'champ-list__item__title', 'champ-list__item__name')
    elif category == 'Vraag 2':
        return get_random_question('champion-abilities.xlsx', 'ability-list__item__name', 'combined')
    # Voeg hier meer categorieën toe als dat nodig is

def show_question_page():
    st.header(st.session_state.current_page)
    st.write('Vraag: ' + st.session_state.question)

    if st.button('Toon antwoord'):
        st.write('Antwoord: ' + st.session_state.answer)
        st.session_state.show_answer = True

    if st.button('Terug'):
        st.session_state.question, st.session_state.answer = None, None
        st.session_state.show_answer = False
        st.session_state.current_page = 'Home'

def main():
    st.title('Vragen en Antwoorden App')

    if 'question' not in st.session_state:
        st.session_state.question = None
    if 'answer' not in st.session_state:
        st.session_state.answer = None
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Home'

    page_options = ['Home', 'Vraag 1', 'Vraag 2']  # Voeg hier meer categorieën toe
    page = st.sidebar.selectbox('Selecteer een pagina:', page_options)

    if page == 'Home':
        st.header('Welkom op de overzichtspagina!')
        st.write('Kies een vraagcategorie hieronder:')
        for category in page_options[1:]:
            if st.button(category):
                st.session_state.question, st.session_state.answer = set_question_and_answer(category)
                st.session_state.show_answer = False
                st.session_state.current_page = category

    elif page.startswith('Vraag'):
        show_question_page()

    if st.session_state.show_answer and page.startswith('Vraag'):
        st.write('Antwoord: ' + st.session_state.answer)

    if page != 'Home':
        if st.button('Opnieuw Vraag'):
            st.session_state.question, st.session_state.answer = set_question_and_answer(st.session_state.current_page)
            st.session_state.show_answer = False

if __name__ == '__main__':
    main()
