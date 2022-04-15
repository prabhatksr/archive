# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:41:56 2022

@author: Admin
"""

import requests
import json
import numpy as np

url = "http://127.0.0.1:4000/prediction"

payload = json.dumps({'uuid': '63f69b2c-8b1c-4740-b78d-52ed9a4515ac',
 'default': 0.0,
 'account_amount_added_12_24m': 0,
 'account_days_in_dc_12_24m': 0.0,
 'account_days_in_rem_12_24m': 0.0,
 'account_days_in_term_12_24m': 0.0,
 'account_incoming_debt_vs_paid_0_24m': 0.0,
 'account_status': 1.0,
 'account_worst_status_0_3m': 1.0,
 'account_worst_status_12_24m': np.nan,
 'account_worst_status_3_6m': 1.0,
 'account_worst_status_6_12m': np.nan,
 'age': 20,
 'avg_payment_span_0_12m': 12.6923076923077,
 'avg_payment_span_0_3m': 8.33333333333333,
 'merchant_category': 'Dietary supplements',
 'merchant_group': 'Health & Beauty',
 'has_paid': True,
 'max_paid_inv_0_12m': 31638.0,
 'max_paid_inv_0_24m': 31638.0,
 'name_in_email': 'no_match',
 'num_active_div_by_paid_inv_0_12m': 0.153846153846154,
 'num_active_inv': 2,
 'num_arch_dc_0_12m': 0,
 'num_arch_dc_12_24m': 0,
 'num_arch_ok_0_12m': 13,
 'num_arch_ok_12_24m': 14,
 'num_arch_rem_0_12m': 0,
 'num_arch_written_off_0_12m': 0.0,
 'num_arch_written_off_12_24m': 0.0,
 'num_unpaid_bills': 2,
 'status_last_archived_0_24m': 1,
 'status_2nd_last_archived_0_24m': 1,
 'status_3rd_last_archived_0_24m': 1,
 'status_max_archived_0_6_months': 1,
 'status_max_archived_0_12_months': 1,
 'status_max_archived_0_24_months': 1,
 'recovery_debt': 0,
 'sum_capital_paid_account_0_12m': 0,
 'sum_capital_paid_account_12_24m': 0,
 'sum_paid_inv_0_12m': 178839,
 'time_hours': 9.65333333333333,
 'worst_status_active_inv': 1.0})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)