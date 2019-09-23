# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 16:41:31 2019

@author: leosa
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing

base_previsores = pd.read_excel('Calculos.xlsx','Simul')
base_comparacional = pd.read_excel('Calculos.xlsx','REAL')
base_previsores = pd.pivot_table(base_previsores, index='Cliente')
base_comparacional = pd.pivot_table(base_comparacional, index='Cliente')

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
base_previsores = scaler.fit_transform(base_previsores)
#base_comparacional = scaler.fit_transform(base_comparacional)
