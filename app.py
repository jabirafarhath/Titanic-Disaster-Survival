import streamlit as st
import pickle
import form

st.title('Titanic Disaster Survival')
st.subheader("This is a prediction system that works on machine learning which predict if the person survived the titanic disaster or not. The accuracy of this prediction is 89%.")
st.write("You can try it by filling a few details in the form we provide.")
form.predict()
