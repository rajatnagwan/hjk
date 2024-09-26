
import streamlit as st
import pickle

# Load the trained model
loaded_model = pickle.load(open('linear_regression_model.sav', 'rb'))

# Create a title for your app
st.title("Monthly Revenue Prediction App")

# Create an input field for the user to enter the monthly revenue
monthly_revenue = st.number_input("Enter Monthly Revenue:", value=0)

# Create a button to trigger the prediction
if st.button("Predict"):
  # Reshape the input to be a 2D array (as expected by the model)
  input_data = [[monthly_revenue]]
  # Make the prediction using the loaded model
  prediction = loaded_model.predict(input_data)
  # Display the prediction to the user
  st.write("Predicted Values:", prediction)

