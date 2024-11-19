import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # Fixed import

# Function to shorten categories based on cutoff
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    return categorical_map

# Function to clean experience values
def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':  # Fixed typo in string
        return 0.5
    return float(x)

# Function to clean education levels
def clean_education(x):
    if 'Bachelor’s degree' in x:
        return "Bachelors degree"
    if "Master’s degree" in x:
        return "Masters degree"
    if "Professional degree" in x or "Other doctoral" in x:
        return "Post grad"
    return "Less than a Bachelors"

# Function to load and clean data
def load_data():  # Fixed function name syntax
    df = pd.read_csv('survey_results_public.csv')
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    df = df[df["Employment"] == "Employed full-time"]

    # Clean the data
    df = df.dropna()  # Drop rows with missing values
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)

    # Shorten country categories
    country_map = shorten_categories(df["Country"].value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 250000]  # Remove extreme values
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]

    return df

df = load_data()  # Correctly call the function

# Function to display the exploration page
def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write(
        """
        ### Stack Overflow Developer Survey 2021
        """
    )

    # Display country distribution
    data = df["Country"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures the pie chart is circular.
    st.write("### Number of Data Points from Different Countries")
    st.pyplot(fig1)

    # Display salary histogram
    st.write("### Mean Salary Based on Country")
    st.bar_chart(df.groupby("Country")["Salary"].mean().sort_values(ascending=True))


