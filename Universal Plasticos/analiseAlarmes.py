import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import matplotlib.pyplot as plt
import math as mt
fp_padrao = 0.92
fp_padrao_Sup = 2-fp_padrao

def normaliza(s):
    if s >= 0:
       return s
    elif s < 0 :
       return s + 2

universal01_dataset = pd.read_excel('universal.xlsx', 'Universal_01')
universal02_dataset = pd.read_excel('universal.xlsx', 'Universal_02')
univ01 = universal01_dataset
univ02 = universal02_dataset

Universal = pd.concat([univ02,univ01])

Universal.drop(columns=['Freqüência', 'Ocorrência'],inplace=True)

Universal.rename(columns ={'Fat,Pot T': 'FP T', 
                            'Fat,Pot, R': 'FP R',
                            'Fat,Pot, S': 'FP S'}, inplace=True)
Universal_p = pd.pivot_table(Universal, index=['Data'])

Universal_p['Pot R KVA'] = (Universal_p['Corrente R'] * Universal_p['Tensão R'] * (mt.sqrt(3)))/1000
Universal_p['Pot S KVA'] = (Universal_p['Corrente S'] * Universal_p['Tensão S'] * (mt.sqrt(3)))/1000
Universal_p['Pot T KVA'] = (Universal_p['Corrente T'] * Universal_p['Tensão T'] * (mt.sqrt(3)))/1000

Universal['Pot R KVA'] = (Universal['Corrente R'] * Universal['Tensão R'] * (mt.sqrt(3)))/1000
Universal['Pot S KVA'] = (Universal['Corrente S'] * Universal['Tensão S'] * (mt.sqrt(3)))/1000
Universal['Pot T KVA'] = (Universal['Corrente T'] * Universal['Tensão T'] * (mt.sqrt(3)))/1000

#Calculo KVAr usando numpy
Universal_p['Pot R KW'] = (Universal_p['Pot R KVA'] * (Universal_p['FP R']))
Universal_p['Pot S KW'] = (Universal_p['Pot S KVA'] * (Universal_p['FP S']))
Universal_p['Pot T KW'] = (Universal_p['Pot T KVA'] * (Universal_p['FP T']))

Universal['Pot R KW'] = (Universal['Pot R KVA'] * (Universal['FP R']))
Universal['Pot S KW'] = (Universal['Pot S KVA'] * (Universal['FP S']))
Universal['Pot T KW'] = (Universal['Pot T KVA'] * (Universal['FP T']))

#Calculo KVAr usando numpy
Universal_p['Pot R KVAr'] = np.sqrt(np.power(Universal_p['Pot R KVA'],2) - np.power(Universal_p['Pot R KW'],2))
Universal_p['Pot S KVAr'] = np.sqrt(np.power(Universal_p['Pot S KVA'],2) - np.power(Universal_p['Pot S KW'],2))
Universal_p['Pot T KVAr'] = np.sqrt(np.power(Universal_p['Pot T KVA'],2) - np.power(Universal_p['Pot T KW'],2))

Universal['Pot R KVAr'] = np.sqrt(np.power(Universal['Pot R KVA'],2) - np.power(Universal['Pot R KW'],2))
Universal['Pot S KVAr'] = np.sqrt(np.power(Universal['Pot S KVA'],2) - np.power(Universal['Pot S KW'],2))
Universal['Pot T KVAr'] = np.sqrt(np.power(Universal['Pot T KVA'],2) - np.power(Universal['Pot T KW'],2))

#Calculo Faltante Kvar
Universal_p['Pot R KVAr faltante'] = (Universal_p['Pot R KVAr']) - (np.sqrt(np.power(Universal_p['Pot R KVA'],2)-
                                                                      (np.power((Universal_p['Pot R KVA'] * (fp_padrao)),2))))
Universal_p['Pot S KVAr faltante'] = (Universal_p['Pot S KVAr']) - (np.sqrt(np.power(Universal_p['Pot S KVA'],2)-
                                                                      (np.power((Universal_p['Pot S KVA'] * (fp_padrao)),2))))
Universal_p['Pot T KVAr faltante'] = (Universal_p['Pot T KVAr']) - (np.sqrt(np.power(Universal_p['Pot T KVA'],2)-
                                                                      (np.power((Universal_p['Pot T KVA'] * (fp_padrao)),2))))

Universal['Pot R KVAr faltante'] = (Universal['Pot R KVAr']) - (np.sqrt(np.power(Universal['Pot R KVA'],2)-
                                                                      (np.power((Universal['Pot R KVA'] * (fp_padrao)),2))))
Universal['Pot S KVAr faltante'] = (Universal['Pot S KVAr']) - (np.sqrt(np.power(Universal['Pot S KVA'],2)-
                                                                      (np.power((Universal['Pot S KVA'] * (fp_padrao)),2))))
Universal['Pot T KVAr faltante'] = (Universal['Pot T KVAr']) - (np.sqrt(np.power(Universal['Pot T KVA'],2)-
                                                                      (np.power((Universal['Pot T KVA'] * (fp_padrao)),2))))
Universal["FP R"] = Universal["FP R"].apply(normaliza)
Universal["FP S"] = Universal["FP S"].apply(normaliza)
Universal["FP T"] = Universal["FP T"].apply(normaliza)

Universal_p["FP R"] = Universal_p["FP R"].apply(normaliza)
Universal_p["FP S"] = Universal_p["FP S"].apply(normaliza)
Universal_p["FP T"] = Universal_p["FP T"].apply(normaliza)

fpfases_abaixo = Universal.loc[((Universal["FP R"]< fp_padrao) | (Universal["FP R"]> fp_padrao_Sup))
                         | ((Universal["FP S"]< fp_padrao) | (Universal["FP S"]> fp_padrao_Sup))
                         | ((Universal["FP T"]< fp_padrao) | (Universal["FP T"]> fp_padrao_Sup))]

fpfases = Universal_p.loc[((Universal_p["FP R"]< fp_padrao) | (Universal_p["FP R"]> fp_padrao_Sup))
                         | ((Universal_p["FP S"]< fp_padrao) | (Universal_p["FP S"]> fp_padrao_Sup))
                         | ((Universal_p["FP T"]< fp_padrao) | (Universal_p["FP T"]> fp_padrao_Sup))]

maximoR = fpfases['Pot R KVAr faltante'].max()
maximoS = fpfases['Pot S KVAr faltante'].max()
maximoT = fpfases['Pot T KVAr faltante'].max()

Valores_ComparacaoR = fpfases[(fpfases['FP R'] > fpfases['FP T'] ) & (fpfases['FP R'] > fpfases['FP T'])]
Valores_ComparacaoS = fpfases[(fpfases['FP S'] > fpfases['FP T'] ) & (fpfases['FP S'] > fpfases['FP T'])]
Valores_ComparacaoT = fpfases[(fpfases['FP T'] > fpfases['FP R'] ) & (fpfases['FP T'] > fpfases['FP S'])]

Universal_p.round(5).to_csv('Universal Leituras.csv')
Universal.round(5).to_csv('Universal.csv')
fpfases.round(5).to_csv('Universal FP FORAS.csv')