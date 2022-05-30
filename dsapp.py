import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(layout='wide')
# Menu option
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Visualizations", 'Try VADER'],  # required
    icons=["house"],  
    menu_icon="cast",  
    default_index=0,  
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white"},  # fafad2
        "icon": {"color": "#eac248", "font-size": "18px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "#eac248",
        },
        "nav-link-selected": {"background-color": "#faf0d2", 'color': '#ea9a48'},
    },
)
if selected == 'Home':
    st.header('Why Streamlit?')
    col1, col2 = st.columns(2)
    with col1:
        with st.expander('Pedagogy'):
            st.write('Data Science can be easy!')
    with col2:
        with st.expander('Visualize'):
            st.write("It's more easy to visualize the dataset and the data!")

# VISUALIZATIONS
if selected == 'Visualizations':
    col3, col4, = st.columns(2)
    col3.subheader('Model 1: Non preprocess data')
    col4.subheader('Model 2: Data preprocessed')
    initial = st.multiselect('What do you want to see?', ['Model1', 'Model2'], ['Model1'])
    #tick = st.checkbox('Show all')
    wc = st.checkbox('Word cloud')
    bc = st.checkbox('Bar chart')
    col5, col6 = st.columns(2)
    col7, col8 = st.columns(2)
    col9, col10 = st.columns(2)
    
# Model 1
    def wc1p():
        col5.image('model1wcpos.PNG')
        col6.write('Model 1, most common positive words')
    def wc1n():
        col7.image('model1wcneg.PNG')
        col8.write('Model 1, most common negative words')
    def bc():
        col9.image('model1countposneg.PNG')
        col10.write('Model 1, barchart of the count of words classificated as positive and negative')

    if 'Model1' in initial:
        if wc:
            wc1p()
            wc1n()
        elif bc:
            bc()
            

# TRY VADER
if selected == 'Try VADER':

    st.title('Sentiment analysis app using VADER')
    st.subheader('Try me!')

    with st.container():
        respuesta = st.text_input(
            'Write a sentence in English to test the sentiment analysis score, you can also add emojis, slang and anglicisms if you want, I am really clever:')

        # respuesta = text.__str__()
        # Transformando la respuesta a string

        sia = SentimentIntensityAnalyzer()

        # For loop para analizar los sentimientos de la frase
        pos_list = []
        neu_list = []
        neg_list = []

        for x in respuesta:
            st.write(f'For the sentence "{respuesta}"')
            polarity = sia.polarity_scores(respuesta)
            pos = polarity["pos"]
            neu = polarity["neu"]
            neg = polarity["neg"]

            # Print of the result
            st.write(f'The percentage of positivity in:"{respuesta}" is : {round(pos * 100, 2)} %')
            st.write(f'The percentage of neutrality in:"{respuesta}" is : {round(neu * 100, 2)} %')
            st.write(f'The percentage of negativity in:"{respuesta}" is : {round(neg * 100, 2)} %')
            st.write("=" * 50)

            # Añado el resultado a una lista
            pos_list.append(round(pos * 100, 2))
            neu_list.append(round(neu * 100, 2))
            neg_list.append(round(neg * 100, 2))
            break
        # if respuesta:
        #     if pos_list[0] <= 30:
        #         st.write("Well, not bad")
        #     elif 31 <= pos_list[0] <= 50:
        #         st.write("Thanks, you are nice :)")
        #     elif 51 >= pos_list[0] <= 65:
        #         st.write("OMG, you are soo nice!")
        #     else:
        #         st.write("Oh, thanks a lot, I really like you! :D")
