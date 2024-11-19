# import streamlit as st
# import pickle
# import numpy as np
# import os
# print(os.path.exists("saved_steps.pkl"))

# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         data = pickle.load(file)
#     return data

# data = load_model()

# regressor = data["model"]
# le_country = data["le_country"]
# le_education = data["le_education"]



# def show_predict_page():
#     st.title("Software Developer Salary Prediction")

#     st.write("""### We need some information to predict the Salary""")

#     countries= (
#         "United States",
#         "India",
#         "United Kingdom",
#         "Germany",
#         "Canada",
#         "Brazil",
#         "France",
#         "Spain",
#         "Netherlands",
#         "Poland",
#         "Italy",
#         "Russian Federation",
#         "Sweden",
#     )

#     education = (
#         "Less than a Bachelors",
#         "Bachelors degree",
#         "Masters degree", 
#         "Post grad",
#     )

#     country = st.selectbox("Country", countries)
#     education = st.selectbox("Education Level", education)

#     experience = st.slider("Years of experience", 0, 50,3)

#     ok = st.button("Compute Salary")

#     if ok:
#         X = np.array([[country, education, experience]])
#         X[:,0] = le_country.transform(X[:,0])
#         X[:,1] = le_education.transform(X[:,1])
#         X = X.astype(float)

#         salary = regressor.predict(X)
#         st.subheader(f"The estimated salary is ${salary[0]:.2f}")


import streamlit as st
import pickle
import numpy as np

# Function to load the model and encoders
def load_model():
    try:
        with open("saved_steps.pkl", "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        st.error("The file 'saved_steps.pkl' was not found. Please check the file path.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

# Load datas
data = load_model()

# Stop execution if data is not loaded
if data is None:
    st.stop()

# Extract the model and encoders from the loaded data
regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Define the prediction page
def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the Salary""")

    # List of countries for the dropdown
    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
    )

    # List of education levels for the dropdown
    education_levels = (
        "Less than a Bachelors",
        "Bachelors degree",
        "Masters degree",
        "Post grad",
    )

    # User inputs
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)
    experience = st.slider("Years of experience", 0, 50, 3)

    # Button to trigger salary computation
    ok = st.button("Compute Salary")

    if ok:
        try:
            # Preprocess user input
            X = np.array([[country, education, experience]])
            X[:, 0] = le_country.transform(X[:, 0])
            X[:, 1] = le_education.transform(X[:, 1])
            X = X.astype(float)

            # Predict salary
            salary = regressor.predict(X)
            st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# Show the prediction page
show_predict_page()
