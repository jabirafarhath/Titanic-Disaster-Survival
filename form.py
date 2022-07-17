from imp import reload
import streamlit as st
import pickle


def load_model():
    reload_model = pickle.load(open('titanic_model.sav', 'rb'))
    return reload_model


def predict():

    passengerId = st.number_input("Passenger Id", 0, 3000)
    pclass = st.selectbox("Ticket Class", {1, 2, 3})
    age = st.slider("Age", 0, 90)
    sibsp = st.number_input(
        "# of Siblings / Spouses aboard the Titanic", 0, 20)
    parch = st.number_input(
        "# of Parents / Children aboard the Titanic", 0, 20)
    fare = st.number_input("Ticket Fare", 0.000, 1000.0000)
    gender = st.radio("Gender", {"Male", "Female", "Other"})
    if gender == 'Male':
        gender = 1
    else:
        gender = 0

    data = [[passengerId, pclass, age, sibsp, parch, fare, gender]]

    ok = st.button("Predict")
    if ok:
        reload_model = load_model()
        result = reload_model.predict(data)
        if result[0] == 1:
            st.write("The person has survived.😄✅")
        else:
            st.write("The person lost his life in the disaster.😥😔")
