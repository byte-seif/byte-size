import streamlit as st
import pandas as pd
import joblib
from utils import preprocessor

def run():
    model = joblib.load(open('model.joblib','rb'))

    st.title("Lab 10.2, Sentiment Analysis Using Streamlit")
    st.text("DON'T TRY TO CONFUSE ME, I'M STILL LEARNING!.")
    st.text("")
    userinput = st.text_input('Enter text below, then click the Predict button.', placeholder='Input text HERE')
    st.text("")
    predicted_sentiment = ""
    if st.button("Predict"):
        predicted_sentiment = model.predict(pd.Series(userinput))[0]
        if predicted_sentiment == 1:
            output = 'positive 👍'
        else:
            output = 'negative 👎'
        sentiment=f'Predicted sentiment of "{userinput}" is {output}.'
        st.success(sentiment)

if __name__ == "__main__":
    run()
