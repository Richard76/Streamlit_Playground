
import streamlit as st
import pandas as pd

def main():
    st.title('Streamlit App')
    st.write('Welcome to this simple Streamlit app.')

    # Load the predictions
    predictions = pd.read_csv('predictions/predict_001.csv')

    # Display the predictions
    st.write('Here are the predictions:')
    st.dataframe(predictions)

if __name__ == '__main__':
    main()
