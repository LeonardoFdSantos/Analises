# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:21:55 2019

@author: leonardo Felipe
"""

import os
import pandas as pd

nomes = pd.read_excel('Valores.xlsx',sheet_name='Pastas')
nomesloop = nomes['Nome']
maximo = nomesloop.count()+1

for i in range(1,maximo):
    nome = nomesloop[:i:]

path = './contas'
for x in nome:
    dir = path+'/'+x
    if os.path.isdir(dir) == False:
        os.makedirs(dir)