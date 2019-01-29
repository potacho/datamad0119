
# ![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# [pandas-project]

## Octavio Garcia Moreno

###### 30/01/2019




## Análisis Inicial de los Datos
Se realiza una codificación del archivo al formato utf-8 previo a su importación. El archivo GSAF5.csv es un fichero que contiene Global Shark Attack Incidents (5992 rows × 24 columns). Dicha información contiene los siguientes atributos (columnas):
- Número de caso (**Case Number**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2'. Sin valor para platear hipótesis.
- Fecha (**Date**): Descripción del momento que ha ocurrido el evento. Es un tipo object muy variado que va desde la fecha exacta (i.e.: 23-Jul-16) hasta un momento indeterminado (i.e. World War II) o incluso 'No date'. Tiene valores nulos mientras que 'Year' no los tiene por lo que se decide trabajar con el atributo 'Year'.
- Año (**Year**): Dato tipo entero que indica el año de ocurrencia del ataque. Se identifican valores que no se corresponden a años.
- Circunstancia (**Type**): Dato tipo object que describe las circunstancias en las que ha ocurrido el ataque. DETERMNAR CUANTOS SON LOS UNNPROVOKED Y HACER DOS GRUPOS DE ANÁLISIS.
- Pais (**Country**): Dato tipo object que indica el país de ocurrencia. SOLO DEJARÍA ESTE DATO?
- Area (**Área**): Dato tipo object que indica la región del pais. NO APORTA MUCHO (VER NULLS).
- Localización (**Location**): Dato tipo object que indica el lugar exacto del evento. NO APORTA MUCHO (VER NULLS).
- Actividad durante el ataque (**Activity**): Dato tipo object que indica la actividad que se estaba realizando durante el ataque. SE PODRIA CORRELACIONAR CON CIRCUNSTANCIA.
- Nombre/Identificación (**Name**): Dato tipo object que identifica a la persona(s) atacadas. NO APORTA MUCHO PARA ANÁLISIS (¿BORRAR?). SE PODRÍA HACER UN ANÁLISIS DE CASOS MULTIPLES VS INDIVIDUOS.
- Género (**Sex**): Dato tipo object que identifica el sexo de la victima. VER NULLS (CASI NINGUNA MUJER?)
- Edad (**Age**): Dato tipo object que indica la edad de la víctima. Hay valores no precisos como '60s' y muchos nulos.
- Tipo de Lesión (**Injury**): Dato tipo object donde se describe el tipo de lesión provocada. Se correlaciona con 'Circunstancia' y 'Fatalidad'. 
- Fatalidad (**Fatal (Y/N**): Dato tipo object que indica 'Y/N'. CONVERTIRLO EN BOOLEANO O LIMPIARLO PARA DIVIDIR.
- Hora (**Time**): Dato tipo object que indica el momento del día en que ocurrió el ataque. Va desde una hora concreta (i.e.: 13h00) hasta un momento del día (i.e.: Afternoon).
- Tipo de Tiburón (**Species**): Dato tipo object que indica el tipo de tiburón y la cantidad de los mismos. MUY VARIADO...NO APORTA MUCHO PARA ANÁLISIS.
- Fuente (**Investigator or Source**): Dato tipo object que describe la fuente de la información (persona o medio informativo). NO APORTA MUCHO - BORRAR 
- Documento asociado (**pdf**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'href formula', 'href', 'Case Number.1', 'Case Number.2'. NO APORTA MUCHO - BORRAR 
- Enlace Informativo (**href formula**): Dato tipo object con el enlace al fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href', 'Case Number.1', 'Case Number.2'. NO APORTA MUCHO - BORRAR 
- Enlace Informativo (**href**): Repite la información de 'href formula'. Probablemente se trate de un Excel que haya generado dos valores al terner hipervinculos a los enlaces. BORRAR
- Identificador de Caso (**Case Number.1**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href formula', 'href', 'Case Number.2'. SIN RELEVANCIA - BORRAR. 
- Identificador de Caso (**Case Number.2**): Columna que repite la información de 'Case Number.2'. BORRAR
- Orden de Ocurrencia ¿Cronológico? (**original order**): Dato tipo entero que indica una especie de orden "cronológico" inverso en el que ocurrieron los eventos. Ojo que el orden no tiene sentido en los casos donde las fechas no están correctamente determinadas. SIN MUCHA RELEVANCIA - BORRAR.
- Atributo sin datos (**Unnamed: 22**). BORRAR.
- Atributo sin datos (**Unnamed: 22**). BORRAR.



```python
import pandas as pd
import numpy as np
fileName = "./GSAF5.csv" 
df1 = pd.read_csv(fileName)
#display(df1.head(1000000))
display(df1.dtypes)
df2 = df1.copy()
```


    Case Number               object
    Date                      object
    Year                       int64
    Type                      object
    Country                   object
    Area                      object
    Location                  object
    Activity                  object
    Name                      object
    Sex                       object
    Age                       object
    Injury                    object
    Fatal (Y/N)               object
    Time                      object
    Species                   object
    Investigator or Source    object
    pdf                       object
    href formula              object
    href                      object
    Case Number.1             object
    Case Number.2             object
    original order             int64
    Unnamed: 22               object
    Unnamed: 23               object
    dtype: object



```python
#display(df2[['Case Number','Date','Year','Type','Country','Area','Location']])
```


```python
#display(df2[['Activity','Name','Sex ','Age','Injury','Fatal (Y/N)','Time']])
```


```python
#display(df2[['Species ','Investigator or Source','pdf','href formula']])
```


```python
#display(df2[['href','Case Number.1','Case Number.2','original order','Unnamed: 22','Unnamed: 23']])
```

### Data Cleaning
Se realizan varias fases de data cleaning:
- **Fase 1:** Eliminación de columnas sin datos y/o con datos repetitivos.
- **Fase 2:** Eliminación de columnas con datos irrelevantes para cualquier análisis (i.e.: códigos de identificación).
- **Fase 3:** Eliminación de registros irrelevantes para el análisis (se hará en la siguiente fase del proyecto).



```python
#Fase 1. Eliminar columnas sin datos o con datos repetidos en otras columnas    
col_f1 = ['href','Case Number.1','Case Number.2','Unnamed: 22','Unnamed: 23']
df3 = df2.drop(col_f1, axis=1)
#display(df3)
#display(df3.dtypes)
```


```python
#Fase 2. Eliminar datos irrelevantes. 
#2.1.Elimino primero las columnas con datos que no aportan valor a los posibles análisis a realizar.

col_f2 = ['Case Number','Investigator or Source','pdf','href formula']
df4 = df3.drop(col_f2, axis=1)
#display(df4)
#display(df4.dtypes)
```


```python
#2.2. Determino columna con un volumen alto de valores null para eliminarlas y acotar las posibles hipótesis.
null_col = df4.isnull().sum()
#null_col[null_col > 0]
display(null_col)
```


    Date                 0
    Year                 0
    Type                 0
    Country             43
    Area               402
    Location           496
    Activity           527
    Name               200
    Sex                567
    Age               2681
    Injury              27
    Fatal (Y/N)         19
    Time              3213
    Species           2934
    original order       0
    dtype: int64



```python
#2.3. Elimino columnas con exceso de nulos teniendo en cuenta que el dataset contiene 5992 registros.
col_f3 = list(null_col[null_col > 1000].index)
df5 = df4.drop(col_f3, axis=1)
#display(df5)
display(df5.dtypes)
```


    Date              object
    Year               int64
    Type              object
    Country           object
    Area              object
    Location          object
    Activity          object
    Name              object
    Sex               object
    Injury            object
    Fatal (Y/N)       object
    original order     int64
    dtype: object



```python
#2.4. Elimino registros duplicados en caso de haberlos. Se utiliza el atributo 'Case Number'.

b = len(df5)
df6 = df5.drop_duplicates()
a = len(df6)
print('Número de registros duplicados eliminados: ', str(b - a))

```

    Número de registros duplicados eliminados:  0



```python
#Atributos relevantes
atributes = ['Date','Year','Type','Country','Area','Location','Activity','Name','Sex ','Injury','Fatal (Y/N)','original order']

#Analisis preliminar de datos para la propuesta de hipótesis.
#print(set(df6['Date']))
print('Date',len(set(df6['Date']))) 
#print(set(df6['Year']))
print('Year',len(set(df6['Year']))) 
print(set(df6['Type']))
print('Type',len(set(df6['Type']))) 
#print(set(df6['Country']))
print('Country',len(set(df6['Country']))) 
#print(set(df6['Area']))
print('Area',len(set(df6['Area']))) 
#print(set(df6['Location']))
print('Location',len(set(df6['Location']))) 
#print(set(df6['Activity']))
print('Activity',len(set(df6['Activity']))) 
#print(set(df6['Name']))
print('Name',len(set(df6['Name']))) 
print(set(df6['Sex ']))
print('Sex ',len(set(df6['Sex '])))
#print(set(df6['Injury']))
print('Injury',len(set(df6['Injury']))) 
print(set(df6['Fatal (Y/N)']))
print('Fatal (Y/N)',len(set(df6['Fatal (Y/N)']))) 
print('Dataset(df6):',len(df6))
```

    Date 5128
    Year 232
    {'Boating', 'Sea Disaster', 'Invalid', 'Unprovoked', 'Provoked', 'Boat'}
    Type 6
    Country 204
    Area 786
    Location 3930
    Activity 1493
    Name 5010
    {nan, 'N', 'F', '.', 'M', 'M ', 'lli'}
    Sex  7
    Injury 3596
    {'Y', nan, 'UNKNOWN', 'N', 'N ', 'F', '#VALUE!', 'n', ' N'}
    Fatal (Y/N) 9
    Dataset(df6): 5992



```python
#Limpieza del atributo Sex

df6[['Sex ','Fatal (Y/N)']] = df6[['Sex ', 'Fatal (Y/N)']].fillna(0)
```


```python
#Analisis del atributo 'Sex '
display(df6.loc[df6['Sex ']=='N',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='.',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='lli',['Year','Name','Sex ','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Sex ']=='F',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='M',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='M ',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4708</th>
      <td>1934</td>
      <td>18' boat, occupants William &amp; Leslie Newton</td>
      <td>N</td>
      <td>No injury to occupants Sharks continually foll...</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5201</th>
      <td>1908</td>
      <td>NaN</td>
      <td>.</td>
      <td>Remains of 3 humans recovered from shark, but ...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1400</th>
      <td>2004</td>
      <td>Brian Kang</td>
      <td>lli</td>
      <td>Lacerations to hand, knee &amp; thigh</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to toes</td>
      <td>N</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>5 tiny puncture marks to lower leg, treated wi...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Buttocks, thigh, left hand &amp; wrist injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2016</td>
      <td>Marin Alice Melton</td>
      <td>F</td>
      <td>Injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>57</th>
      <td>2016</td>
      <td>Maria Korcsmaros \n</td>
      <td>F</td>
      <td>Injuries to arm and shoulder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>59</th>
      <td>2016</td>
      <td>Mary Marcus</td>
      <td>F</td>
      <td>Puncture wounds to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>60</th>
      <td>2016</td>
      <td>Krystal Magee</td>
      <td>F</td>
      <td>Lacerations and puncture wounds to foot and ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>61</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Back, arm &amp; hand injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Arm grabbed PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2016</td>
      <td>J. Orr</td>
      <td>F</td>
      <td>Minor injury to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>89</th>
      <td>2016</td>
      <td>Patricia Howe</td>
      <td>F</td>
      <td>Avulsion injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Foot nipped</td>
      <td>N</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2016</td>
      <td>Kaya Waldman</td>
      <td>F</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2015</td>
      <td>Cristina Ojeda-Thies</td>
      <td>F</td>
      <td>Lacerations to left forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>111</th>
      <td>2015</td>
      <td>Tamsin Scott</td>
      <td>F</td>
      <td>Lacerations to both hands and forearms</td>
      <td>N</td>
    </tr>
    <tr>
      <th>113</th>
      <td>2015</td>
      <td>female</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2015</td>
      <td>Ryla Underwood</td>
      <td>F</td>
      <td>Lower left leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>118</th>
      <td>2015</td>
      <td>Jill Kruse</td>
      <td>F</td>
      <td>Injury to right ankle/calf &amp; hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>129</th>
      <td>2015</td>
      <td>Meti Kershner</td>
      <td>F</td>
      <td>Laceration to forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>137</th>
      <td>2015</td>
      <td>female</td>
      <td>F</td>
      <td>Laceration to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>146</th>
      <td>2015</td>
      <td>Caterina Gennaro</td>
      <td>F</td>
      <td>No injury, shark struck board, tossing her int...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>150</th>
      <td>2015</td>
      <td>Jane Neame</td>
      <td>F</td>
      <td>Left foot &amp; ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>152</th>
      <td>2015</td>
      <td>Elinor Dempsey</td>
      <td>F</td>
      <td>No injury, surfboard bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>157</th>
      <td>2015</td>
      <td>Kaley Szarmack</td>
      <td>F</td>
      <td>Lacerations to right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5435</th>
      <td>1892</td>
      <td>Mrs. Coe</td>
      <td>F</td>
      <td>Abrasions to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5508</th>
      <td>1886</td>
      <td>2 women</td>
      <td>F</td>
      <td>The body of one woman had been bitten by a sha...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5529</th>
      <td>1884</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL            Leg severed by harpooned shar...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5533</th>
      <td>1884</td>
      <td>Miss Warren</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5569</th>
      <td>1880</td>
      <td>a widow</td>
      <td>F</td>
      <td>Hands, forearm &amp; left thigh lacerated, radial ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5574</th>
      <td>1880</td>
      <td>Teresa Bonnell</td>
      <td>F</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5595</th>
      <td>1878</td>
      <td>Dolores Margarita Corrales y Roa</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5610</th>
      <td>1877</td>
      <td>female</td>
      <td>F</td>
      <td>Ankle injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5698</th>
      <td>1862</td>
      <td>The widowed Marchioness of Lendinez</td>
      <td>F</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5705</th>
      <td>1862</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5730</th>
      <td>1855</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>F</td>
      <td>Death preceded shark involvement</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5760</th>
      <td>1849</td>
      <td>Mrs. Cracton</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5798</th>
      <td>1834</td>
      <td>Kaugatava Orurutm</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5799</th>
      <td>1832</td>
      <td>Aboriginal female</td>
      <td>F</td>
      <td>Leg severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5832</th>
      <td>1800</td>
      <td>NaN</td>
      <td>F</td>
      <td>FATAL, all onboard were killed by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5833</th>
      <td>1791</td>
      <td>female, an Australian aboriginal</td>
      <td>F</td>
      <td>FATAL, "bitten in two"</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5879</th>
      <td>0</td>
      <td>Lassie</td>
      <td>F</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5883</th>
      <td>0</td>
      <td>Martha Hatagouei</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>0</td>
      <td>female</td>
      <td>F</td>
      <td>Leg severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>0</td>
      <td>Danniell Washington</td>
      <td>F</td>
      <td>Severe abrasion to forearm from captive shark ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5896</th>
      <td>0</td>
      <td>Sametra Mestri</td>
      <td>F</td>
      <td>Hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5910</th>
      <td>0</td>
      <td>female, a Hae Nyeo</td>
      <td>F</td>
      <td>FATAL, injured while diving, then shark bit her</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5913</th>
      <td>0</td>
      <td>female</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5918</th>
      <td>0</td>
      <td>Jill Reed</td>
      <td>F</td>
      <td>Shoulder scratched, swim fin bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5921</th>
      <td>0</td>
      <td>woman</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>585 rows × 5 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Puncture wounds to foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>Michael Dornellas</td>
      <td>M</td>
      <td>Face bruised when partly blind shark collided ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2016</td>
      <td>Mark Davis</td>
      <td>M</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2016</td>
      <td>Roger Brissom</td>
      <td>M</td>
      <td>Fin of hooked shark injured fisherman's forear...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4835 rows × 5 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>341</th>
      <td>2014</td>
      <td>male</td>
      <td>M</td>
      <td>Laceration &amp; puncture wounds to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1363</th>
      <td>2005</td>
      <td>Ben Edelstein</td>
      <td>M</td>
      <td>Severe injury to lower leg</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>



```python
#Analisis del atributo 'Fatal (Y/N)'
display(df6.loc[df6['Fatal (Y/N)']=='UNKNOWN',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='#VALUE!',['Year','Name','Sex ','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Fatal (Y/N)']=='Y',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='N',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='N ',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']==' N',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='n',['Year','Name','Sex ','Injury','Fatal (Y/N)']])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>401</th>
      <td>2013</td>
      <td>female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1047</th>
      <td>2008</td>
      <td>Jamie Adlington</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1142</th>
      <td>2007</td>
      <td>Alex Takyi</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2025</th>
      <td>1997</td>
      <td>Jos\E9 Luiz Lipiani</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2035</th>
      <td>1997</td>
      <td>Gersome Perreno</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2042</th>
      <td>1996</td>
      <td>Blair Hall</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2070</th>
      <td>1996</td>
      <td>Trimurti Day</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2082</th>
      <td>1996</td>
      <td>Wayne Leong</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2098</th>
      <td>1996</td>
      <td>Marris</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2103</th>
      <td>1995</td>
      <td>Carlton Taniyama</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2163</th>
      <td>1995</td>
      <td>Hutchins</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2179</th>
      <td>1995</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2184</th>
      <td>1994</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2317</th>
      <td>1992</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2423</th>
      <td>1990</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2425</th>
      <td>1989</td>
      <td>Ryan Johnson</td>
      <td>M</td>
      <td>No details, "recovering in Darwin Hospital"</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2436</th>
      <td>1989</td>
      <td>John Benson</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2581</th>
      <td>1986</td>
      <td>Crawford</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2657</th>
      <td>1984</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2675</th>
      <td>1984</td>
      <td>Greenwood</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2718</th>
      <td>1983</td>
      <td>Arnold Schwarzwood</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2771</th>
      <td>1982</td>
      <td>Giovanni Vuoso</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2773</th>
      <td>1982</td>
      <td>English holiday-maker</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2781</th>
      <td>1981</td>
      <td>Robert Conklin</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2813</th>
      <td>1981</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2816</th>
      <td>1981</td>
      <td>Filmer</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2982</th>
      <td>1975</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3073</th>
      <td>1973</td>
      <td>G. Cole</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3171</th>
      <td>1970</td>
      <td>David Vota</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3186</th>
      <td>1970</td>
      <td>Mr. Jurincic</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4977</th>
      <td>1923</td>
      <td>John Hayes</td>
      <td>M</td>
      <td>Death may have been due to drowning</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4987</th>
      <td>1922</td>
      <td>H.R.W.</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5014</th>
      <td>1921</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Buttons &amp; shoes found in shark caught in fish ...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5038</th>
      <td>1919</td>
      <td>5 cadets from the Naval training ship Tingara</td>
      <td>M</td>
      <td>Shark involvement not confirmed</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5097</th>
      <td>1915</td>
      <td>Remains of male found in shark</td>
      <td>M</td>
      <td>Fatal, drowning or scavenging</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5114</th>
      <td>1914</td>
      <td>Indian female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5120</th>
      <td>1913</td>
      <td>NaN</td>
      <td>M</td>
      <td>Man's leg recovered from 800-lb shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5121</th>
      <td>1913</td>
      <td>NaN</td>
      <td>F</td>
      <td>Female foot recovered from shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5134</th>
      <td>1912</td>
      <td>arm recovered from hooked shark</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5173</th>
      <td>1910</td>
      <td>Lieut. James H. Stewart</td>
      <td>M</td>
      <td>Calf removed, not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5308</th>
      <td>1901</td>
      <td>boy</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5316</th>
      <td>1900</td>
      <td>George Brown</td>
      <td>M</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5355</th>
      <td>1898</td>
      <td>male</td>
      <td>M</td>
      <td>Unknown</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5373</th>
      <td>1897</td>
      <td>Anonymous</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5411</th>
      <td>1894</td>
      <td>Catherine Beach</td>
      <td>F</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5414</th>
      <td>1894</td>
      <td>Erskine H. Reynolds</td>
      <td>M</td>
      <td>"Painfully injured" but no details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5432</th>
      <td>1893</td>
      <td>No details</td>
      <td>NaN</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5464</th>
      <td>1890</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5465</th>
      <td>1890</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5726</th>
      <td>1856</td>
      <td>a seaman from the John and Lucy</td>
      <td>M</td>
      <td>Severe bite to thigh. Not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5795</th>
      <td>1836</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>No details, it was the year the first settlers...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5845</th>
      <td>1755</td>
      <td>Fishermen</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5856</th>
      <td>1638</td>
      <td>sailors</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5857</th>
      <td>1637</td>
      <td>Hindu pilgrims</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5858</th>
      <td>1617</td>
      <td>Indian people</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5860</th>
      <td>1595</td>
      <td>male</td>
      <td>M</td>
      <td>Leg severed mid-thigh, hand severed, arm above...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5862</th>
      <td>1555</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5863</th>
      <td>1554</td>
      <td>males (wearing armor)</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
  </tbody>
</table>
<p>94 rows × 5 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5461</th>
      <td>1890</td>
      <td>Joseph Lundy</td>
      <td>M</td>
      <td>Forensic evidence indicated death resulted fro...</td>
      <td>#VALUE!</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>56</th>
      <td>2016</td>
      <td>Ben Gerring</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>83</th>
      <td>2016</td>
      <td>Maika Tabua</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>108</th>
      <td>2015</td>
      <td>Adrian Esteban Rafael</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>164</th>
      <td>2015</td>
      <td>Damien Johnson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2015</td>
      <td>Yves Berthelot</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>208</th>
      <td>2015</td>
      <td>Margaret Cruse</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2015</td>
      <td>Elio Canestri</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2015</td>
      <td>Eugenio Masala</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>219</th>
      <td>2015</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>226</th>
      <td>2015</td>
      <td>Talon Bishop</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>227</th>
      <td>2015</td>
      <td>Tadashi Nakahara</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>242</th>
      <td>2014</td>
      <td>Jay Muscat</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>248</th>
      <td>2014</td>
      <td>Daniel Smith</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>251</th>
      <td>2014</td>
      <td>Rameshwar Ram Dhauro</td>
      <td>M</td>
      <td>FATAL, arm bitten by shark hauled on deck     ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>278</th>
      <td>2014</td>
      <td>Paul Wilcox</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>303</th>
      <td>2014</td>
      <td>Cuban refugees</td>
      <td>M</td>
      <td>Shark involvement prior to death not confirmed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2014</td>
      <td>John Petty</td>
      <td>M</td>
      <td>Missing after a dive, shark involvement consid...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>347</th>
      <td>2014</td>
      <td>Christine Armstrong</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>348</th>
      <td>2014</td>
      <td>Michael McGregor</td>
      <td>M</td>
      <td>Shark bites may have been post mortem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>349</th>
      <td>2014</td>
      <td>Friedrich Burgstaller.</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>360</th>
      <td>2014</td>
      <td>Sam Kellett</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>373</th>
      <td>2013</td>
      <td>Patrick Briney</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>374</th>
      <td>2013</td>
      <td>Zac Young</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>376</th>
      <td>2013</td>
      <td>Chris Boyd</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>390</th>
      <td>2013</td>
      <td>Burgert Van Der Westhuizen</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>416</th>
      <td>2013</td>
      <td>Jana Lutteropp</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5942</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5943</th>
      <td>0</td>
      <td>an Indian</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5944</th>
      <td>0</td>
      <td>Sandrillio</td>
      <td>M</td>
      <td>FATAL, hip bitten  PROVOKED INCIDENT</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5948</th>
      <td>0</td>
      <td>Gilbertese fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>C.</td>
      <td>NaN</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5952</th>
      <td>0</td>
      <td>an old fisherman</td>
      <td>M</td>
      <td>FATAL, foot lacerated &amp; crushed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5953</th>
      <td>0</td>
      <td>a local dignitary</td>
      <td>M</td>
      <td>FATAL, femoral artery severed, died 12 days la...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5954</th>
      <td>0</td>
      <td>I.A.S. C. driver</td>
      <td>M</td>
      <td>FATAL, fell into water when shark seized his r...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5955</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL, left leg bitten with severe blood loss</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5956</th>
      <td>0</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>FATAL, died of sepsis</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>20 Fijians</td>
      <td>NaN</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>1552 rows × 5 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Occupant: Ben Stratton</td>
      <td>NaN</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Occupant: Ben Raines</td>
      <td>NaN</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5928</th>
      <td>0</td>
      <td>Dalton Baldwin</td>
      <td>M</td>
      <td>No injury, bumped by shark which took speared ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5929</th>
      <td>0</td>
      <td>Les Bishop</td>
      <td>M</td>
      <td>Bumped by sharks</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5931</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Right hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5932</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Arm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5933</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Right leg lacerated &amp; surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5934</th>
      <td>0</td>
      <td>male, a sponge Diver</td>
      <td>M</td>
      <td>Lower leg and forearm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5936</th>
      <td>0</td>
      <td>Ross Doe</td>
      <td>M</td>
      <td>Shoulder abraded by skin of shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5939</th>
      <td>0</td>
      <td>Horton Chase</td>
      <td>M</td>
      <td>Abrasions &amp; bruises hip to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5940</th>
      <td>0</td>
      <td>John Fenton</td>
      <td>M</td>
      <td>Shark bit diver's sleeve after he patted it on...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5945</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5946</th>
      <td>0</td>
      <td>Dusty Rhodes</td>
      <td>M</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5947</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5950</th>
      <td>0</td>
      <td>American male</td>
      <td>M</td>
      <td>Buttock bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5951</th>
      <td>0</td>
      <td>Mortakee</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5957</th>
      <td>0</td>
      <td>a fisherman / diver</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>4315 rows × 5 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5191</th>
      <td>1909</td>
      <td>anonymous</td>
      <td>NaN</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3716</th>
      <td>1960</td>
      <td>Mrs. Despo Snow-Christensen</td>
      <td>F</td>
      <td>Shark brushed past, minor injuries if any</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3718</th>
      <td>1960</td>
      <td>Lester McDougall</td>
      <td>M</td>
      <td>Left thigh lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3720</th>
      <td>1960</td>
      <td>Harry Bicknell</td>
      <td>M</td>
      <td>Right shoulder lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3722</th>
      <td>1960</td>
      <td>Ken O\92Connell</td>
      <td>M</td>
      <td>Shark knocked him off surf-ski, he inhaled wat...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>1960</td>
      <td>Don Morrissey</td>
      <td>M</td>
      <td>Scratches on right upper arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>1960</td>
      <td>Fisheries trainee</td>
      <td>M</td>
      <td>Left wrist bitten by netted shark placed in bo...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>1960</td>
      <td>B. Hooper</td>
      <td>M</td>
      <td>Swept off rocks &amp; presumed to have drowned, sh...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3730</th>
      <td>1960</td>
      <td>NaN</td>
      <td>M</td>
      <td>Injuries to leg &amp; foot</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Year</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5779</th>
      <td>1842</td>
      <td>male</td>
      <td>NaN</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
  </tbody>
</table>
</div>


Hola


```python

```
