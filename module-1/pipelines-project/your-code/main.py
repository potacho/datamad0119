#Funciones principales del pipeline
import os

import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

fileName = "./datos.csv" 
df_original = pd.read_csv(fileName)
df_raw_raw = df_original.copy()

#Eliminación de duplicados
def duplicates(df_raw_raw):
    b = len(df_raw_raw)
    df_raw = df_raw_raw.drop_duplicates()
    a = len(df_raw)
    if str(b - a) == 0:
        return df_raw
    else:
        return print('El numero de duplicados eliminados no es cero. Es necesario analizar los datos')

'''
#Análisis de nulos
null_col = df_raw.isnull().sum()
display(null_col)


# ### Limpieza de datos
# Realizo limpieza de los datos:
# 
# - Elimino columna 'HDI for year' ya que contiene un 70% de valores nulos.
# - Elimino columna 'country-year' ya que son datos redundantes. 
# - Elimino columna 'gdp_for_year' ya que son datos tipo 'object' con los que no se puede trabajar numéricamente y con el gdp per capita se pueden proponer mejores hipótesis.

# In[15]:


col_clean = ['country-year','HDI for year',' gdp_for_year ($) ']
df_clean = df_raw.drop(col_clean, axis=1)
display(df_clean.head())


# ### Hipótesis
# Este  data set permite realizar varias propuestas de hipótesis al respecto del fenómeno de los suicidios en todo el mundo durante los últimos 30 años:
# 
# - Se pueden presentar gráficamente los ratios de suicidio ('suicides/100k pop') por diferentes criterios: país, género y rango de edad. 
# - Se pueden generar 'bins' dentro de diferentes atributos y compararlos: zonas geográficas (e.g.: continentes), eṕocas (e.g.: 1985-1995, 1996-2009,...), generaciones, 
# - Se pueden establecer relaciones con los valores numericos como la población o GDP per capita y buscar algún tipo de correlación.

# In[ ]:





# ### Data wrangling
# Realizo varias acciones de transformación de los datos:
# 
# - Cambio la denominación de las columnas para mejor manejo y posterior presentación en informes.
# - Analizo los datos en detalle para verificar que no haya inconsistencias antes de pla

# In[16]:


#Renombro columnas para mejor manejo y posterior generación de informes.
df_w1 = df_clean.rename(index=str, columns={'country':'Country','year':'Year','sex':'Gender','age':'Ages',
                                            'suicides_no':'Suicides','population':'Population',
                                            'suicides/100k pop':'Suicidesx100k','gdp_per_capita ($)':'GDPxCapita',
                                            'generation':'Generation'})
display(df_w1.head())


# In[17]:


#Analizo los datos en busqueda de inconsistencias
atributes = ['Country','Year','Gender','Ages','Suicides','Population','Suicidesx100k','GDPxCapita','Generation']
#print(set(df_w1['Country']))
print('Country',len(set(df_w1['Country']))) 
print(set(df_w1['Year']))
print('Year',len(set(df_w1['Year']))) 
print(set(df_w1['Gender']))
print('Gender',len(set(df_w1['Gender']))) 
print(set(df_w1['Ages']))
print('Ages',len(set(df_w1['Ages']))) 
#print(set(df_w1['Suicides']))
print('Suicides',len(set(df_w1['Suicides']))) 
#print(set(df_w1['Population']))
print('Population',len(set(df_w1['Population']))) 
#print(set(df_w1['Suicidesx100k']))
print('Suicidesx100k',len(set(df_w1['Suicidesx100k']))) 
#print(set(df_w1['GDPxCapita']))
print('GDPxCapita',len(set(df_w1['GDPxCapita']))) 
print(set(df_w1['Generation']))
print('Generation',len(set(df_w1['Generation']))) 
display(df_w1.head())


# In[18]:


#Se detecta que la columna 'Generation' es inconsistente (no se corresponde adecuadamente con la columna 'Ages') 
#por lo que la eliminamos
col_inconsist = ['Generation']
df_w2 = df_w1.drop(col_inconsist, axis=1)
col_useless = ['Suicides','Population','GDPxCapita']
df_w3 = df_w2.drop(col_useless, axis=1)

rows = list(set(df_w3['Country']))

r_north = ['Iceland','Sweden','Norway','Finland','Denmark','Norway','Netherlands']
     
r_south = ['Spain','Greece','Italy','Portugal','France']

r_n_s = r_north+r_south


# In[37]:


df_north = df_w3[df_w3['Country'].isin(r_north)]
display(df_north)
df_south = df_w3[df_w3['Country'].isin(r_south)]
display(df_south)
#df = df_w3[df_w3['Country'].isin(r_n_s)]
#df = pd.concat([df_north,df_south])
#display(df)


# In[38]:


#Bins decades
decade_labels = ['1985-1995', '1996-2006', '2007-2016']
cutoffs = [1985,1996,2007,2016]
north_bins = pd.cut(df_north['Year'], cutoffs, labels=decade_labels)
south_bins = pd.cut(df_south['Year'], cutoffs, labels=decade_labels)


# In[42]:


df_north['Decades'] = north_bins
df_dec_north = df_north.groupby(['Decades','Country']).sum().drop(['Year'], axis=1)
display(df_dec_north)
df_south['Decades'] = south_bins
df_dec_south = df_south.groupby(['Decades','Country']).sum().drop(['Year'], axis=1)
display(df_dec_south)


# In[50]:


df_eu_north = df_dec_north.groupby("Decades").agg({"Suicidesx100k":"mean"})
display(df_eu_north)
df_eu_south = df_dec_south.groupby("Decades").agg({"Suicidesx100k":"mean"})
display(df_eu_south)


# In[52]:


height = list(df_eu_north["Suicidesx100k"])
bars = tuple(df_eu_north.index)
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['blue'])
plt.xticks(y_pos, bars)
plt.savefig("North", bbox_inches='tight')

height = list(df_eu_south["Suicidesx100k"])
bars = tuple(df_eu_south.index)
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=['red'])
plt.xticks(y_pos, bars)
plt.savefig("South", bbox_inches='tight')


# ### IDEAS

# In[1]:


#Statistics
#stats = df_w2.describe().transpose()
#display(stats.head())


# In[13]:


#Pivot table
table_country = pd.pivot_table(df_w2, values='Suicides', index=['Country'], columns=['Ages'],aggfunc=np.sum)
display(table_country.head())


# In[31]:


#Reporte de datos de Sx100k 
col_country = ['Year','Population','Suicides','GDPxCapita']
df_w3 = df_w2.drop(col_country, axis=1)
df_country = df_w3.groupby(['Country','Ages']).sum()
display(df_country.sort_values(by=['Country','Ages'], ascending=False).head())


# In[ ]:





# In[88]:


#df_country es el data frame de partida ordenado por paises.
df_n_s = df.groupby(['Country','Ages']).sum()
df_n_s.sort_values(by=['Country'], ascending=False).head(100)
'''
