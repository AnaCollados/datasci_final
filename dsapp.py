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
        with st.expander("It's easy"):
            st.write("""
            Streamlit is an open-source app framework which is particularly used for Machine Learning and Data Science. In this sense, 
            Streamlit is very useful for building various applications with the help of very few lines of code, thus is considered as a very beginner-friendly tool.
            """)
    with col2:
        with st.expander('Visualize'):
            st.write("""
            Streamlit has been considered to served in this project, as an app deployer. In other sense, the main purpose of using Streamlit was to 
            facilitate the experience with the project. In the end, this purpose could not be fully accomplished due to the lack of time employed.""")

# VISUALIZATIONS
if selected == 'Visualizations':
    col3, col4, = st.columns(2)
    col3.subheader('Model 1: Non preprocess data')
    col4.subheader('Model 2: Data preprocessed')
    initial = st.multiselect('What do you want to see?', ['Model1', 'Model2'], ['Model1'])
    #tick = st.checkbox('Show all')
    #wc = st.checkbox('Word cloud')
    #bc = st.checkbox('Bar chart')
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
        wc1p()
        wc1n()
        bc()
    
    col11, col12 = st.columns(2)
    col13, col14 = st.columns(2)
    col15, col16 = st.columns(2)      
    #MODEL 2
    def bc2():
        col11.image('model2bc.PNG')
        col12.write('Model 2, barchart of the count of words classificated as positive and negative')
    def wc2p():
        col13.image('model2wcpos.PNG')
        col14.write('Model 2, most common positive words')    
    def wc2n():
        col15.image('model2wcneg.PNG')
        col16.write('Model 2, most common negative words')
    
    if 'Model2' in initial:
        wc2p()
        wc2n()
        bc2()
            
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
