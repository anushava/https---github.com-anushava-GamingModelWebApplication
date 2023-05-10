# FastAPI is a Web framework for developing RESTful APIs in Python
# Uvicorn is an ASGI web server implementation for Python
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle
import joblib
import numpy as np
import json

# Load the model
model = pickle.load(open("model\predict_customer_deposit_model.pkl", 'rb'))

#Create the FastAPI Instance
app = FastAPI()

# create the input schema using pydantic basemodel
class Input(BaseModel):
    Tenure : float
    Deposit : float
    Turnover : float
    Withdrawal : float  

# create routes
# create home route(/) which will just return “Predictor” message and predict route(/predict)
@app.get("/")
def read_root():
    return{"msg":"Customer Deposit Predictor"}

@app.post("/predict")
def predit_price(input:Input):
    data = input.dict()
    data_in = [[data['Tenure'],data['Deposit'],data['Turnover'],data['Withdrawal']]]
    scaler = joblib.load('model\scaler.save')
    data_in = scaler.transform(data_in) 
    predictions = model.predict(data_in)
    
    return {"predictions":predictions.item(0)}

# call http://127.0.0.1:8000/docs
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
