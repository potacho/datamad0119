
from tkinter import *
# esta ha sido la solución: sudo apt-get install python3-tk
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use("agg")
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

def colOut(df_raw)
null_col = df_raw.isnull().sum()
display(null_col)


print('funciona')