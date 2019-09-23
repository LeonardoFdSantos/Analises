# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 14:22:17 2019

@author: ENERGENS_04
"""

import pandas as pd
import xlsxwriter
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns

base_br = pd.read_excel('Alarmes.xlsx' , 'BR')
base_eu = pd.read_excel('Alarmes.xlsx' , 'EU')
base = pd.concat([base_eu, base_br])

base.columns

base.drop(['Clearance Type' , 'Alarm ID' , 'Location Information', 'Column1'] , axis=1 , inplace=True)

base_new = base.loc[(base['Alarm Severity'] == "Major") & (base['Alarm Name'] == "Grid Overvoltage\t") & (base['PV Plant'] == 'Cassio_Burin\t')]
base_new.columns
base_new['PV Plant'].value_counts()
base_new['PV Plant'].value_counts().plot.barh()

base_nova = base.loc[(base['Alarm Severity'] == "Major") & (base['Alarm Name'] == "Grid Overvoltage\t") & (base['PV Plant'] != 'Cassio_Burin\t')]
base_nova['PV Plant'].value_counts()
base_nova['PV Plant'].value_counts().plot.barh()

#writer = pd.ExcelWriter('Alarmes Analise.xlsx', engine='xlsxwriter')
#base_new.to_excel(writer, sheet_name='dados Alarmes')
#writer.save()

base_con = base.loc[(base['Alarm Severity'] == "Minor") & (base['Alarm Name'] == "Communication Fault\t")]
base_con['PV Plant'].value_counts()
base_con['PV Plant'].value_counts().plot.barh()

base_unica = pd.DataFrame()
base_unica['Alarmes de Comunicação'] = base_con['PV Plant'].value_counts()
base_unica['Alertas RGE Overvoltage'] = base_nova['PV Plant'].value_counts()
base_unica['Alertas Fora RGE Overvoltage'] = base_new['PV Plant'].value_counts()
base_unica['Alertas Fora RGE Overvoltage'].plot.barh()
base_unica['Alertas RGE Overvoltage'].plot.barh()
#base_Unica['Alarmes de Comunicação']base_unica['Alarmes de Comunicação']> 50).plot.barh()
