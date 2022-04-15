# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 13:01:58 2022

@author: Admin
"""

import uvicorn
import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

class Music(BaseModel):
    account_amount_added_12_24m : int
    account_days_in_rem_12_24m : float
    avg_payment_span_0_12m : float
    has_paid : bool
    num_active_div_by_paid_inv_0_12m : float
    num_arch_dc_0_12m : int
    num_arch_ok_12_24m : int
    num_arch_written_off_0_12m : float
    num_unpaid_bills : int
    status_2nd_last_archived_0_24m : int
    status_max_archived_0_6_months : int
    status_max_archived_0_24_months : int
    sum_capital_paid_account_0_12m : int
    sum_paid_inv_0_12m : int
    account_days_in_dc_12_24m : float
    account_days_in_term_12_24m : float
    merchant_category : str
    max_paid_inv_0_12m : float
    num_active_inv : int
    num_arch_dc_12_24m : int
    num_arch_rem_0_12m : int
    num_arch_written_off_12_24m : float
    status_last_archived_0_24m : int
    status_3rd_last_archived_0_24m : int
    status_max_archived_0_12_months : int
    recovery_debt : int
    sum_capital_paid_account_12_24m : int
    time_hours : float
    age : int
    merchant_group : str
    max_paid_inv_0_24m : float
    num_arch_ok_0_12m : int
    name_in_email : str


app = FastAPI()


with open("./model", "rb") as f:

    model = joblib.load(f)

with open('./preprocessor', 'rb') as f:
    preprocessor = joblib.load(f)
    
    
@app.get('/')
def index():

    return {'message': 'This is the homepage of the API '}

@app.post('/prediction')
def get_music_category(data: Music):

    received = data.dict()
    
    series = pd.Series(received)
    df = pd.DataFrame(series).T
    
    X = preprocessor.transform(df)
    probability = model.predict_proba(X)

    return {'Probability': probability}

if __name__ == '__main__':

    uvicorn.run(app, host='127.0.0.1', port=4000, debug=True)
    
    