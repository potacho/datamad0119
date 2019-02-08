#Importación de los módulos.
from tkinter import *
# esta ha sido la solución: sudo apt-get install python3-tk
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

#Lectura de los datos y creación del dataframe. 
fileName = "./datos.csv" 
df_original = pd.read_csv(fileName)

#Se hace una copia del dataframe para no corromper los datos originales.
df_raw_raw = df_original.copy()
#print(df_raw_raw.head())

'''
#Eliminación de duplicados
def duplicates(df_raw_raw):
    b = len(df_raw_raw)
    df_raw = df_raw_raw.drop_duplicates()
    a = len(df_raw)
    if str(b - a) == 0:
        return df_raw
    else:
        return print('El numero de duplicados eliminados no es cero. Es necesario analizar los datos')

def colOut(df_raw)
null_col = df_raw.isnull().sum()
display(null_col)
'''

#Tipo de datos en cada columna (atributos).
#print(df_raw_raw.dtypes)

#Análisis de duplicados (no hay duplicados).
b = len(df_raw_raw)
df_raw = df_raw_raw.drop_duplicates()
a = len(df_raw)
#print('Número de registros duplicados eliminados: ', str(b - a))

#Análisis de nulos. Solo hay una columna con nulos pero está en torno al 70% de los valores.
null_col = df_raw.isnull().sum()
#print(null_col)

#Elimino las columnas indicadas en la descripción de arriba.
col_clean = ['country-year','HDI for year',' gdp_for_year ($) ']
df_clean = df_raw.drop(col_clean, axis=1)
#print(df_clean.head())

#Renombro columnas para mejor manejo y posterior generación de informes.
df_w1 = df_clean.rename(index=str, columns={'country':'Country','year':'Year','sex':'Gender','age':'Ages',
                                            'suicides_no':'Suicides','population':'Population',
                                            'suicides/100k pop':'Suicidesx100k','gdp_per_capita ($)':'GDPxCapita',
                                            'generation':'Generation'})
#print(df_w1.head())

#Analizo los datos en busqueda de inconsistencias y/o datos que no me son útiles para mi análisis.
atributes = ['Country','Year','Gender','Ages','Suicides','Population','Suicidesx100k','GDPxCapita','Generation']
#print(set(df_w1['Country']))
#print('Country',len(set(df_w1['Country']))) 
#print(set(df_w1['Year']))
#print('Year',len(set(df_w1['Year']))) 
#print(set(df_w1['Gender']))
#print('Gender',len(set(df_w1['Gender']))) 
#print(set(df_w1['Ages']))
#print('Ages',len(set(df_w1['Ages']))) 
#print(set(df_w1['Suicides']))
#print('Suicides',len(set(df_w1['Suicides']))) 
#print(set(df_w1['Population']))
#print('Population',len(set(df_w1['Population']))) 
#print(set(df_w1['Suicidesx100k']))
#print('Suicidesx100k',len(set(df_w1['Suicidesx100k']))) 
#print(set(df_w1['GDPxCapita']))
#print('GDPxCapita',len(set(df_w1['GDPxCapita']))) 
#print(set(df_w1['Generation']))
#print('Generation',len(set(df_w1['Generation'])))

#Se detecta que la columna 'Generation' es inconsistente (no se corresponde adecuadamente con la columna 'Ages'). 
#Se elimina ya que no aporta nada.
#Se exporta fichero .csv 'limpio' que se puede utilizar para análisis posteriores.
col_inconsist = ['Generation']
df_w2 = df_w1.drop(col_inconsist, axis=1)
df_w2.to_csv('/home/potacho/github/datamad0119/module-1/pipelines-project/your-code/datos_cw.csv', 
             index=False, encoding = 'utf-8')
df_w2.head()

#También se eliminan las columnas que no van a formar parte del análisis.
#IMPORTANTE: estas columnas pueden ser utilizadas para el planteamiento de otras hipótesis (df_w2)
col_useless = ['Suicides','Population','GDPxCapita']
df_w3 = df_w2.drop(col_useless, axis=1)
df_w3.head()

#Se crean los 2 dataframes (north y south)
r_north = ['Iceland','Sweden','Norway','Finland','Denmark','Norway','Netherlands']
r_south = ['Spain','Greece','Italy','Portugal','France']
r_n_s = r_north+r_south
df_north = df_w3[df_w3['Country'].isin(r_north)]
#print(df_north.head())
df_south = df_w3[df_w3['Country'].isin(r_south)]
#print(df_south.head())
#rows = list(set(df_w3['Country']))
#df = df_w3[df_w3['Country'].isin(r_n_s)]
#df = pd.concat([df_north,df_south])
#display(df)

#Se crean los bins correspondientes a las decadas
decade_labels = ['1985-1995', '1996-2006', '2007-2016']
cutoffs = [1985,1996,2007,2016]
north_bins = pd.cut(df_north['Year'], cutoffs, labels=decade_labels)
south_bins = pd.cut(df_south['Year'], cutoffs, labels=decade_labels)

#Se agrupan los datos por decadas para north. Esta sería una de las salidas (parámetro -n) enviando un .html.
df_north['Decades'] = north_bins
df_dec_north = df_north.groupby(['Decades','Country']).sum().drop(['Year'], axis=1)
#print(df_dec_north.head(50))
#df_dec_north.to_html(open('north.html', 'w'))

#Se agrupan los datos por decadas para south. Esta sería una de las salidas (parámetro -s) enviando un .html.
df_south['Decades'] = south_bins
df_dec_south = df_south.groupby(['Decades','Country']).sum().drop(['Year'], axis=1)
#print(df_dec_south.head(50))
#df_dec_south.to_html(open('south.html', 'w'))

#Se agrupan los datos realizando una media para cada una de las regiones para realizar la comparativa.
df_eu_north = df_dec_north.groupby("Decades").agg({"Suicidesx100k":"mean"})
#print(df_eu_north)
df_eu_south = df_dec_south.groupby("Decades").agg({"Suicidesx100k":"mean"})
#print(df_eu_south)

#Se genera gráfico que compara las dos regiones por décadas. Se envía gráfico por email (parámetro -c).
height = list(df_eu_north["Suicidesx100k"])
bars = tuple(df_eu_north.index)
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['blue'])
plt.xticks(y_pos, bars)
#plt.savefig("North", bbox_inches='tight')
height = list(df_eu_south["Suicidesx100k"])
bars = tuple(df_eu_south.index)
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['red'])
plt.xticks(y_pos, bars)
#plt.savefig("NorthVsSouth", bbox_inches='tight')

print('\n\nSe han procesado los datos satisfactoriamente!!!\n\n')

import argparse
import subprocess 
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--north", help="envia datos del norte de europa", action="store_true")
parser.add_argument("-s", "--south", help="envia datos del sur de europa", action="store_true")
parser.add_argument("-c", "--northvssouth", help="envia comparativa entre el norte y el sur de europa", action="store_true")
args = parser.parse_args()
if args.north:
    df_dec_north.to_html(open('north.html', 'w'))
    msg = "Se adjunta tabla que incluye el resultado del análisis de los datos del norte de Europa"
    command = 'echo {} | mail --attach=/home/potacho/github/datamad0119/module-1/pipelines-project/your-code/north.html -s "Evolucion de los suicidios en el Norte de Europa" "potacho@gmail.com"'.format(msg)
    subprocess.Popen(command, shell=True)
    print("Se ha enviado un correo electrónico con los resultados a potacho@gmail.com\n")
elif args.south:
    df_dec_south.to_html(open('south.html', 'w'))
    msg = "Se adjunta tabla que incluye el resultado del análisis de los datos del sur de Europa"
    command = 'echo {} | mail --attach=/home/potacho/github/datamad0119/module-1/pipelines-project/your-code/south.html -s "Evolucion de los suicidios en el Sur de Europa" "potacho@gmail.com"'.format(msg)
    subprocess.Popen(command, shell=True)
    print("Se ha enviado un correo electrónico con los resultados a potacho@gmail.com\n")
elif args.northvssouth:
    plt.savefig("NorthVsSouth", bbox_inches='tight')
    msg = "Se adjunta gráfico que incluye una comparativa entre el Norte y el Sur de Europa"
    command = 'echo {} | mail --attach=/home/potacho/github/datamad0119/module-1/pipelines-project/your-code/NorthVsSouth.png -s "Evolucion de los suicidios en Europa Occidental" "potacho@gmail.com"'.format(msg)
    subprocess.Popen(command, shell=True)
    print("Se ha enviado un correo electrónico con los resultados a potacho@gmail.com\n")


