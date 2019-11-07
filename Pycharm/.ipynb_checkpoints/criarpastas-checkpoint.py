# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:21:55 2019

@author: leosa
"""

import os
import pandas as pd
import numpy as np
nomes = pd.read_excel('Valores.xlsx',sheet_name='Pastas')
nomes
nomesloop = nomes['Nome']
maximo = nomesloop.count()+1
maximo

for i in range(1,maximo):
    nome = nomesloop[:i:]

path = './contas'
for x in nome:
    dir = path+'/'+x
    os.makedirs(dir)