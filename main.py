import streamlit as st

st.title("Ticketing Machine")

#gets the number of adults and children from the user
no_of_adults = st.number_input("Number of Adults", min_value=0, step=1)
no_of_children = st.number_input("Number of Children", min_value=0, step=1)



st.write("total cost of tickets: $", no_of_adults * 20 + no_of_children * 10)