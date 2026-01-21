import streamlit as st
import pandas as pd
import joblib

# Load pre-trained models and preprocessors
preprocessor = joblib.load('preprocessor.pkl')
model = joblib.load('random_forest_model.pkl')

# Streamlit app title
st.title('Network Intrusion Detection System')

# Function to identify categorical and numerical columns
def identify_columns(df):
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    return categorical_cols, numerical_cols

# Load the dataset
data = pd.read_csv('Test_data.csv')
categorical_cols, numerical_cols = identify_columns(data)

# Collecting user inputs
user_input = {}

for col in categorical_cols:
    options = data[col].unique().tolist()
    user_input[col] = st.selectbox(f'Select {col}', options)

for col in numerical_cols:
    user_input[col] = st.number_input(f'Enter {col}', value=float(data[col].mean()))

# Predict button
if st.button('Predict'):
    # Preprocess and predict
    input_df = pd.DataFrame([user_input])
    input_processed = preprocessor.transform(input_df)
    prediction = model.predict(input_processed)

    # Display prediction
    st.subheader('Prediction')
    st.write(prediction)

# About section
st.sidebar.header("About")
st.sidebar.info("This is a demo app for network intrusion detection using machine learning.")
