# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:44:23 2019

@author: ENERGENS_04
"""
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import matplotlib.pyplot as plt
import math as mt

ValoresDataset = pd.read_excel('Analise.xlsx', 'Valores')
Valores = ValoresDataset
import featuretools as ft

data = ft.demo.load_mock_customer()
customers_df = data["customers"]
sessions_df = data["sessions"]
transactions_df = data["transactions"]
entities = {"customers" : (customers_df, "customer_id"),
            "sessions" : (sessions_df, "session_id", "session_start"),
            "transactions" : (transactions_df, "transaction_id", "transaction_time")
}