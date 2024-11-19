#import streamlit as st
#from predict_page import show_predict_page

#st.selectbox("Explore or Predict", ("Predict", "Explore"))

#show_predict_page()


import streamlit as st
from predict_page import show_predict_page
# Assuming you have an 'explore_page' function or similar

# Capture the user's selection
page = st.selectbox("Explore or Predict", ("Predict", "Explore"))

# Conditional logic to display content
if page == "Predict":
    show_predict_page()
elif page == "Explore":
    # Replace with the appropriate function for 'Explore'
    st.write("Explore content goes here.")
