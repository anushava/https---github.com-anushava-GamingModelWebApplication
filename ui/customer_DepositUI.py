# Develop Front-end UI using Streamlit
# Streamlit is an open source app framework in Python language. It helps us create web apps
# complete ML app with API and UI

import streamlit as st
import requests 
import json
import joblib

# The requests module allows you to send HTTP requests using Python
# The HTTP request returns a Response Object with all the response data.
def main():
    st.title("Customer Deposit Predictor")
    tenure = st.number_input("Tenure")
    deposit = st.number_input("Deposit")
    turnover = st.number_input("Turnover")
    withdrawal = st.number_input("Withdrawal")
    
    # now create the dictionary for all those values which we have to pass to API
    input_data={
        "Tenure":tenure,
        "Deposit":deposit,
        "Turnover":turnover,
        "Withdrawal":withdrawal
    }
    # Now call the API with request module with post method, URL we have got in previous step and input data
    price = 0
    if st.button("Predict"):
        price = requests.post(url="http://127.0.0.1:8000/predict", data=json.dumps(input_data))
        price = price.json()
        p = price["predictions"]
        st.success(f'The Predicted Deposit over the next 30 days is {p}')

     # Now, finally call main method using
if __name__ == "__main__":
    main()   


