
# ![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# [pandas-project]

## Octavio Garcia Moreno

###### 30/01/2019




## Análisis Inicial de los Datos
Se realiza una codificación del archivo al formato utf-8 previo a su importación. El archivo GSAF5.csv es un fichero que contiene Global Shark Attack Incidents (5992 rows × 24 columns). Dicha información contiene los siguientes atributos (columnas):
- Número de caso (**Case Number**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href formula', 'href', 'Case Number.1', 'Case Number.2'. Sin valor para platear hipótesis.
- Fecha (**Date**): Descripción del momento que ha ocurrido el evento. Es un tipo object muy variado que va desde la fecha exacta (i.e.: 23-Jul-16) hasta un momento indeterminado (i.e. World War II) o incluso 'No date'. Tiene valores nulos mientras que 'Year' no los tiene por lo que se decide trabajar con el atributo 'Year'.
- Año (**Year**): Dato tipo entero que indica el año de ocurrencia del ataque. Se identifican valores que no se corresponden a años (i.e.: 'Year' = 0).
- Circunstancia (**Type**): Dato tipo object que describe las circunstancias en las que ha ocurrido el ataque. Potencial atributo a analizar.
- Pais (**Country**): Dato tipo object que indica el país de ocurrencia. 
- Area (**Área**): Dato tipo object que indica la región del pais. 
- Localización (**Location**): Dato tipo object que indica el lugar exacto del evento. 
- Actividad durante el ataque (**Activity**): Dato tipo object que indica la actividad que se estaba realizando durante el ataque. Se podría usar para correlacionar y corregir errores en 'Type'.
- Nombre/Identificación (**Name**): Dato tipo object que identifica a la persona(s) atacadas. Indica nombre y/o descripción del o los individuos.
- Género (**Sex**): Dato tipo object que identifica el sexo de la victima. 
- Edad (**Age**): Dato tipo object que indica la edad de la víctima. Hay valores no precisos como '60s' y muchos nulos.
- Tipo de Lesión (**Injury**): Dato tipo object donde se describe el tipo de lesión provocada. Se correlaciona con 'Circunstancia' y 'Fatalidad'. 
- Fatalidad (**Fatal (Y/N**): Dato tipo object que indica 'Y/N', en caso de que haya sido fatal o no el ataque.
- Hora (**Time**): Dato tipo object que indica el momento del día en que ocurrió el ataque. Va desde una hora concreta (i.e.: 13h00) hasta un momento del día (i.e.: Afternoon).
- Tipo de Tiburón (**Species**): Dato tipo object que indica el tipo de tiburón y la cantidad de los mismos. 
- Fuente (**Investigator or Source**): Dato tipo object que describe la fuente de la información (persona o medio informativo). 
- Documento asociado (**pdf**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'href formula', 'href', 'Case Number.1', 'Case Number.2'. 
- Enlace Informativo (**href formula**): Dato tipo object con el enlace al fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href', 'Case Number.1', 'Case Number.2'. 
- Enlace Informativo (**href**): Repite la información de 'href formula'. Probablemente se trate de un Excel que haya generado dos valores al terner hipervinculos a los enlaces.
- Identificador de Caso (**Case Number.1**): Dato tipo object con el nombre del fichero .pdf con la información sobre el ataque. Se correlaciona con 'pdf', 'href formula', 'href', 'Case Number.2'. 
- Identificador de Caso (**Case Number.2**): Columna que repite la información de 'Case Number.2'. 
- Orden de Ocurrencia ¿Cronológico? (**original order**): Dato tipo entero que indica una especie de orden "cronológico" inverso en el que ocurrieron los eventos. Ojo que el orden no tiene sentido en los casos donde las fechas no están correctamente determinadas. 
- Atributo sin datos (**Unnamed: 22**). 
- Atributo sin datos (**Unnamed: 22**).



```python
#Importo los módulos para trabajar y el fichero .csv ya codificado como UTF-8 (realicé codificación en NotePad)
import pandas as pd
import numpy as np
fileName = "./GSAF5.csv" 
df1 = pd.read_csv(fileName)
#display(df1.head(1000000))
display(df1.dtypes)
df2 = df1.copy()
#Se identifican 24 columnas todas tipo 'object' excepto 2 que son tipo 'int'
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
#Visualización de los datos para análisis inicial
#display(df2[['Case Number','Date','Year','Type','Country','Area','Location']])
```


```python
#Visualización de los datos para análisis inicial
#display(df2[['Activity','Name','Sex ','Age','Injury','Fatal (Y/N)','Time']])
```


```python
#Visualización de los datos para análisis inicial
#display(df2[['Species ','Investigator or Source','pdf','href formula']])
```


```python
#Visualización de los datos para análisis inicial
#display(df2[['href','Case Number.1','Case Number.2','original order','Unnamed: 22','Unnamed: 23']])
```

### Data Cleaning
Se realizan varias fases de data cleaning:
- **Fase 1:** Eliminación de columnas sin datos y/o con datos repetitivos.
- **Fase 2:** Eliminación de columnas con datos irrelevantes para cualquier análisis (i.e.: códigos de identificación).
- **Fase 3:** Corrección de registros (exceso de nulos, duplicados, valores con erratas, unificación,...).



```python
#Fase 1. Eliminar columnas sin datos o con datos repetidos en otras columnas    
col_f1 = ['href','Case Number.1','Case Number.2','Unnamed: 22','Unnamed: 23']
df3 = df2.drop(col_f1, axis=1)
#display(df3)
#display(df3.dtypes)
```


```python
#Fase 2. Elimino las columnas con datos que no aportan valor a las posibles hipótesis a realizar.
col_f2 = ['Case Number','Investigator or Source','pdf','href formula']
df4 = df3.drop(col_f2, axis=1)
#display(df4)
#display(df4.dtypes)
```


```python
#Fase 3. Eliminación de nulos (identificación).
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
##Fase 3. Eliminación de nulos teniendo en cuenta que el dataset contiene 5992 registros.
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
##Fase 3. Eliminación de duplicados.
b = len(df5)
df6 = df5.drop_duplicates()
a = len(df6)
print('Número de registros duplicados eliminados: ', str(b - a))
```

    Número de registros duplicados eliminados:  0


### Data Manipulation
Se plantea la circunstancia de una ONG dedicada a la conservación de la vida marina que quiere mostrar como ha sido la evolución de los ataques de tiburones a lo largo de la historia registrada y cual puede ser la influencia de la invasión humana en el entorno de los tiburones en la incidencia de ataques, así como también la evolución de la fatalidad en los ataques a lo largo del tiempo. Para ello se establece una primera aproximación creando 3 bins de datos separados por eras historicas modernas. Tras la fase de limpieza se pasa de 24 a 12 atributos.


```python
#Atributos relevantes. Se analizan los valores de cada atributo para detectar aquellos más trabajables
#(Este paso fue previo y necesario para el planteamiento de las hipotesis del proyecto)
atributes = ['Date','Year','Type','Country','Area','Location','Activity','Name','Sex ','Injury','Fatal (Y/N)','original order']
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
    {'Boating', 'Unprovoked', 'Invalid', 'Boat', 'Sea Disaster', 'Provoked'}
    Type 6
    Country 204
    Area 786
    Location 3930
    Activity 1493
    Name 5010
    {'M ', 'F', 'lli', 'N', 'Nulos', 'M', '.'}
    Sex  7
    Injury 3596
    {'#VALUE!', 'F', 'N', 'UNKNOWN', ' N', 'Y', 'Nulos', 'n', 'N '}
    Fatal (Y/N) 9
    Dataset(df6): 5992


### Atributos Relevantes
Se seleccionan los atributos más relevantes para el planteamiento de hipótesis y se "manipulan" para extraer información. Lo atributos seleccionados son:
- Año (**'Year'**)
- Circunstancia (**'Type**)
- Género (**'Sex'**)
- Fatalidad (**'Fatal (Y/N)'**)


```python
#Sustitución de NaN en 'Sex ' y 'Fatal (Y/N)'
df6[['Sex ','Fatal (Y/N)']] = df6[['Sex ', 'Fatal (Y/N)']].fillna('Nulos')
print(set(df6['Type']))
print('Type',len(set(df6['Type']))) 
print(set(df6['Sex ']))
print('Sex ',len(set(df6['Sex '])))
print(set(df6['Fatal (Y/N)']))
print('Fatal (Y/N)',len(set(df6['Fatal (Y/N)']))) 
```

    {'Boating', 'Unprovoked', 'Invalid', 'Boat', 'Sea Disaster', 'Provoked'}
    Type 6
    {'M ', 'F', 'lli', 'N', 'Nulos', 'M', '.'}
    Sex  7
    {'#VALUE!', 'F', 'N', 'UNKNOWN', ' N', 'Y', 'Nulos', 'n', 'N '}
    Fatal (Y/N) 9



```python
#Analisis del atributo 'Type'
display(df6.loc[df6['Type']=='Unprovoked',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Type']=='Boating',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Type']=='Provoked',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Type']=='Boat',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Type']=='Sea Disaster',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Type']=='Invalid',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>Surfing</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>Surfing</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Wading</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Swimming</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>Kite surfing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>Boogie boarding</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>Surfing</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>Body boarding</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>Spearfishing</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>Surfing</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>Surfing</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>Wading</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>Snorkeling</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>SUP Foil boarding</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>Surfing</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>Swimming</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>Surfing</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>Surfing</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>Spearfishing</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Surfing</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>NaN</td>
      <td>Minor injury to toes</td>
      <td>N</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Puncture wounds to foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Michael Dornellas</td>
      <td>Scuba Diving</td>
      <td>Face bruised when partly blind shark collided ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Wading</td>
      <td>5 tiny puncture marks to lower leg, treated wi...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5957</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a fisherman / diver</td>
      <td>Diving</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>Diving</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Bathing</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>Sponge diving</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>Standing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>Wading</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>Pearl diving</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>Swimming in pool formed by construction of a w...</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>Fishing</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>Swimming around anchored ship</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Crew swimming alongside their anchored ship</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>4 men were bathing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>Wreck of  large double sailing canoe</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>Swimming</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>Fishing</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>Wading</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>Swimming</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>NaN</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>Fishing</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>Fishing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>Fishing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Diving</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>Pearl diving</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4386 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4025</th>
      <td>1956</td>
      <td>Boating</td>
      <td>Manuel Pereira</td>
      <td>Longling fishing</td>
      <td>FATAL. Shark sank fishing boat, causing death ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>4027</th>
      <td>1956</td>
      <td>Boating</td>
      <td>multiple boats including B.J. C. Brunt</td>
      <td>Fishing</td>
      <td>No injury, sharks bit propellers, etc</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4030</th>
      <td>1956</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Boating</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4047</th>
      <td>1955</td>
      <td>Boating</td>
      <td>yacht Even</td>
      <td>Ocean racing</td>
      <td>No injury to occupants, shark gouged hull</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4048</th>
      <td>1955</td>
      <td>Boating</td>
      <td>boat, occupants: P.D. Neilly &amp; Charlton Anderson</td>
      <td>Fishing for pompano</td>
      <td>No injury to occupants, shark released from ne...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4063</th>
      <td>1955</td>
      <td>Boating</td>
      <td>launch, occupant: Clarrie Whelan</td>
      <td>Fishing</td>
      <td>Whelan's head was injured when he fell to the ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4080</th>
      <td>1955</td>
      <td>Boating</td>
      <td>racing scull, occupants: Bill Andrews on bow o...</td>
      <td>Rowing</td>
      <td>No injury to occupants; shark grabbed oar, vau...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4081</th>
      <td>1955</td>
      <td>Boating</td>
      <td>10' row boat occupants;  Douglas Richards &amp; Ge...</td>
      <td>Rowing toward snapper grounds</td>
      <td>No injury to occupants, 6 sharks charged boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4097</th>
      <td>1954</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Boating</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4107</th>
      <td>1954</td>
      <td>Boating</td>
      <td>10 crew</td>
      <td>Fishing trawler Flavio Gioia</td>
      <td>No injury to occupants. Shark tore nets &amp; traw...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>4148</th>
      <td>1953</td>
      <td>Boating</td>
      <td>12' to 14' dory, occupants: John D. Burns &amp; Jo...</td>
      <td>Fishing for lobsters</td>
      <td>Burns drowned as result of attack on boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4152</th>
      <td>1953</td>
      <td>Boating</td>
      <td>16' launch</td>
      <td>NaN</td>
      <td>No injury to occupant. As engine started, shar...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4164</th>
      <td>1953</td>
      <td>Boating</td>
      <td>14-foot boat Sintra</td>
      <td>Fishing</td>
      <td>No injury to occupant, shark charged boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4178</th>
      <td>1952</td>
      <td>Boating</td>
      <td>a skill. Occupants George Lunsford &amp; 2 companions</td>
      <td>Fishing for trout</td>
      <td>No injury to occupants. Shark chasing fish lea...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4187</th>
      <td>1952</td>
      <td>Boating</td>
      <td>25' cutter</td>
      <td>Fishing for white sharks</td>
      <td>No injury to fisherman Alf Dean &amp; other occupa...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4233</th>
      <td>1950</td>
      <td>Boating</td>
      <td>A canoe; occupants Harry Goodson &amp; Douglas Barnes</td>
      <td>Paddling a canoe</td>
      <td>No injury to occupants, shark holed canoet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4238</th>
      <td>1950</td>
      <td>Boating</td>
      <td>40' fishing cutter</td>
      <td>Fishing</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4248</th>
      <td>1950</td>
      <td>Boating</td>
      <td>Remo Adriani</td>
      <td>Fishing on a boat</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4258</th>
      <td>1950</td>
      <td>Boating</td>
      <td>Neil Drake</td>
      <td>Sitting on side of dinghy mending a net</td>
      <td>No injury to occupant, shark bit side of dinghy</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4290</th>
      <td>1949</td>
      <td>Boating</td>
      <td>boat</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4295</th>
      <td>1949</td>
      <td>Boating</td>
      <td>male</td>
      <td>Fishing, on a boat</td>
      <td>No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4331</th>
      <td>1948</td>
      <td>Boating</td>
      <td>boat  Marie</td>
      <td>Fishing</td>
      <td>No injury to occupants, boat holed by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4335</th>
      <td>1947</td>
      <td>Boating</td>
      <td>10' dinghy</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark made 20 to 30 ru...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4349</th>
      <td>1947</td>
      <td>Boating</td>
      <td>12-foot dinghy Occupants: R. Hunt &amp; a friend.</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bumped &amp; lifted ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4357</th>
      <td>1947</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Fishing</td>
      <td>No injury, shark holed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4360</th>
      <td>1947</td>
      <td>Boating</td>
      <td>rowboat, occupants: Bob Scott &amp; John Blackwell</td>
      <td>Rowing</td>
      <td>No injury, shark lifted the boat 0.5 m out of ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4363</th>
      <td>1946</td>
      <td>Boating</td>
      <td>Moored fishing launch of Harry Lone</td>
      <td>NaN</td>
      <td>Shark jumped into cockpit</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4374</th>
      <td>1946</td>
      <td>Boating</td>
      <td>boat, occupants: C. Nardelli &amp; son</td>
      <td>Fishing</td>
      <td>No injury to occupants. Shark charged boat, to...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4375</th>
      <td>1946</td>
      <td>Boating</td>
      <td>14' catamaran, occupant: M. Leverenz</td>
      <td>Fishing</td>
      <td>No injury; shark rammed boat, catapulting Leve...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4385</th>
      <td>1946</td>
      <td>Boating</td>
      <td>4 boats</td>
      <td>NaN</td>
      <td>No injury to occupants, shark struck boats+K1581</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>4971</th>
      <td>1923</td>
      <td>Boating</td>
      <td>J. Rigby</td>
      <td>After rowing skiff was holed by shark, he was ...</td>
      <td>FATAL, taken by shark. Two other men drowned, ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>4972</th>
      <td>1923</td>
      <td>Boating</td>
      <td>boat, occupants; Carl Sjoistrom &amp; 2 other crew</td>
      <td>Dismantling cable buoys of the cable ship All ...</td>
      <td>No injury to occupants, shark rammed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4980</th>
      <td>1923</td>
      <td>Boating</td>
      <td>boat, occupant: Richard Rodney</td>
      <td>Fishing</td>
      <td>No injury to occupant Shark struck boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4990</th>
      <td>1922</td>
      <td>Boating</td>
      <td>boat, occupants:  Mr. Goslin &amp; 4 passengers</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark splintered stern</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5043</th>
      <td>1919</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Fishing</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5105</th>
      <td>1914</td>
      <td>Boating</td>
      <td>Occupants: Ivan Angjus &amp; Stevo Kentera</td>
      <td>Fishing boat</td>
      <td>No injury, shark bit paddle and stern of boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5155</th>
      <td>1911</td>
      <td>Boating</td>
      <td>2 fishermen</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bit boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5264</th>
      <td>1905</td>
      <td>Boating</td>
      <td>skiff, occupants: Russel J. Coles and others</td>
      <td>Harpooning turtles</td>
      <td>No injury, shark bumped skifft</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5292</th>
      <td>1902</td>
      <td>Boating</td>
      <td>Row boat; occupants - 2 young men</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark grabbed anchor r...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5342</th>
      <td>1899</td>
      <td>Boating</td>
      <td>boat, occupants: 2 Jacksonville pilots</td>
      <td>Rowing</td>
      <td>No injury to occupants. shark bit oar</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5374</th>
      <td>1896</td>
      <td>Boating</td>
      <td>10' skiff. Occupants F. Whitehead &amp; L. Honeybone</td>
      <td>Fishing</td>
      <td>No injury to occupants. Shark bit boat several...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5404</th>
      <td>1895</td>
      <td>Boating</td>
      <td>oar of Knut Dahl's boat</td>
      <td>NaN</td>
      <td>No injury to occupants of boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5462</th>
      <td>1890</td>
      <td>Boating</td>
      <td>Salvatore &amp; Agostino Bugeja</td>
      <td>Fishing boat with 4 men on board was rammed &amp; ...</td>
      <td>FATAL, 2 men were lost, presumed taken by the ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5482</th>
      <td>1888</td>
      <td>Boating</td>
      <td>catboat. Occupants: Captain Tuppe &amp; 2 young la...</td>
      <td>Sailing</td>
      <td>No injury to occupants. Shark beat away with oar</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5486</th>
      <td>1888</td>
      <td>Boating</td>
      <td>2 men</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark holed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5490</th>
      <td>1888</td>
      <td>Boating</td>
      <td>Burke</td>
      <td>Rowing</td>
      <td>Shark bit boat, but no injury to occupant who ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5498</th>
      <td>1887</td>
      <td>Boating</td>
      <td>Mr. Boucaut &amp; Mr. Harris</td>
      <td>Rowing a dinghy</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5504</th>
      <td>1886</td>
      <td>Boating</td>
      <td>boat, occupants: 4 men</td>
      <td>NaN</td>
      <td>Shark attacked boat, shark killed &amp; towed to s...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5506</th>
      <td>1886</td>
      <td>Boating</td>
      <td>John Parker &amp; Edward Matthews</td>
      <td>Clamming</td>
      <td>No injury. They were chased by three sharks, o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5514</th>
      <td>1886</td>
      <td>Boating</td>
      <td>20' boat; occupants: John Wright &amp; a friend</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark shook boat "stem...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5519</th>
      <td>1885</td>
      <td>Boating</td>
      <td>boat, occupant John Bishop</td>
      <td>NaN</td>
      <td>No injury to occupant, shark bit off section o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5563</th>
      <td>1881</td>
      <td>Boating</td>
      <td>male</td>
      <td>Fishing on a boat</td>
      <td>Non-Fatal</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5567</th>
      <td>1880</td>
      <td>Boating</td>
      <td>Captain Aleck Robertson</td>
      <td>Sailing</td>
      <td>Shark bit stern, no injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5573</th>
      <td>1880</td>
      <td>Boating</td>
      <td>boat, Occupants: William Smith &amp; Thomas Martin</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark rammed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5627</th>
      <td>1874</td>
      <td>Boating</td>
      <td>2 occupants</td>
      <td>Fishing</td>
      <td>Shark damaged boat, but no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5628</th>
      <td>1874</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Fishing</td>
      <td>Shark and boat collided. No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5633</th>
      <td>1874</td>
      <td>Boating</td>
      <td>A dory: occupants : 2 men</td>
      <td>Fishing</td>
      <td>Shark bit &amp; tipped the dory</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5635</th>
      <td>1874</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Fleet of canoes caught by a squall and charged...</td>
      <td>2 people out of +70 survived, one of whom was ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5678</th>
      <td>1865</td>
      <td>Boating</td>
      <td>boat: 4 occupants</td>
      <td>Fishing</td>
      <td>FATAL: Boat capsized, sharks took fishermen</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5679</th>
      <td>1865</td>
      <td>Boating</td>
      <td>R.H. Barrett, pilot holding steering oar of wh...</td>
      <td>Boarding a ship</td>
      <td>No injury to pilot, oar bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>110 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>Lobstering</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>Fishing</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Roger Brissom</td>
      <td>Fishing</td>
      <td>Fin of hooked shark injured fisherman's forear...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Nathan Oliver</td>
      <td>Fishing</td>
      <td>Right thigh injured by hooked pregnant female ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Brad Vale</td>
      <td>Spearfishing</td>
      <td>No injury but shark punctured his wetsuit afte...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>female</td>
      <td>Teasing a shark</td>
      <td>Arm grabbed PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing</td>
      <td>Foot bitten by landed shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>70</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Teva Tokoragi</td>
      <td>Spearfishing</td>
      <td>Severe lacerations to right forearm, hand and ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>80</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Henry Kreckman</td>
      <td>NaN</td>
      <td>Minor injury to chest PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>147</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Dylan Marks</td>
      <td>Kayak Fishing</td>
      <td>Laceration to dorsum of foot by hooked shark  ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>160</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Richard Shafer</td>
      <td>Spearfishing</td>
      <td>Right hand bitten  PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>165</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Austin Lorber</td>
      <td>Kayak Fishing</td>
      <td>No injury to occupant. Kayak bitten by gaffed ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>184</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Stephen</td>
      <td>Swimming</td>
      <td>Minor lacerations to forearm when he grabbed s...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>223</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>David Villegas Mora</td>
      <td>Fishing</td>
      <td>Right hand bitten by hooked shark PROVOKED INC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>231</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Michael Pollard</td>
      <td>Shark fishing</td>
      <td>Lacerations to calf by hooked shark PROVOKED I...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>246</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing</td>
      <td>Laceration to calf when he fell on shark he ha...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>249</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing for blue sharks</td>
      <td>Glancing bite to wrist from netted shark PROVO...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>251</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Rameshwar Ram Dhauro</td>
      <td>Fishing</td>
      <td>FATAL, arm bitten by shark hauled on deck     ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>259</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Ryan Hunt</td>
      <td>Surfing</td>
      <td>Laceration to dorsum of left foot when he step...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>281</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing</td>
      <td>Bitten twice on the leg by a shark he was atte...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>286</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Mathew Vickers</td>
      <td>Fishing</td>
      <td>Lacerations to foot by hooked shark PROVOKED I...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>290</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>John Wiley</td>
      <td>Fishing for sharks</td>
      <td>Lacerations to forearm from hooked shark PROVO...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>313</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Steve Robles</td>
      <td>Swimming</td>
      <td>PROVOKED INCIDENT Torso bitten by shark hooked...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>320</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Ric Wright</td>
      <td>Petting a shark</td>
      <td>Lacerations to right hand by captive shark PRO...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>331</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Teasing a shark</td>
      <td>Cut to tip of finger by a captive shark PROVOK...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>344</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Lionel McDougall</td>
      <td>Fishing</td>
      <td>Lacerations to leg &amp; hand by hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>361</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Simon Torres</td>
      <td>Fishing</td>
      <td>Possibly a PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>363</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Richard O'Connor</td>
      <td>Fishing</td>
      <td>Lacerations to ring and pinky fingers of his l...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>379</th>
      <td>2013</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Shark fishing</td>
      <td>Injuries to arm &amp; leg by hooked shark   PROVOK...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>395</th>
      <td>2013</td>
      <td>Provoked</td>
      <td>Erez Lev</td>
      <td>Diving</td>
      <td>Hand bitten PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5363</th>
      <td>1897</td>
      <td>Provoked</td>
      <td>a sailor</td>
      <td>Angling</td>
      <td>Hooked shark bit his leg PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5366</th>
      <td>1897</td>
      <td>Provoked</td>
      <td>"Hoke" Smith</td>
      <td>Fishing</td>
      <td>Lacerations to hand by netted shark PROVOKED I...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5390</th>
      <td>1895</td>
      <td>Provoked</td>
      <td>open boat, occupants: Robert Ruark, Hoyle Dosh...</td>
      <td>Fishing</td>
      <td>No injury, hooked shark rammed boat &amp; Ruark fe...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5405</th>
      <td>1894</td>
      <td>Provoked</td>
      <td>Chatiles F. Brynes</td>
      <td>Fishing</td>
      <td>Left leg bitten PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5410</th>
      <td>1894</td>
      <td>Provoked</td>
      <td>William Muller</td>
      <td>Fishing</td>
      <td>Laceration to calf  PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5442</th>
      <td>1892</td>
      <td>Provoked</td>
      <td>Christopher Wang</td>
      <td>Fishing</td>
      <td>Lacerations to calf by netted shark PROVOKED I...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5443</th>
      <td>1892</td>
      <td>Provoked</td>
      <td>Mr. A. Rotaman</td>
      <td>Dress diving</td>
      <td>FATAL         Bitten in two by shark that he m...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5448</th>
      <td>1891</td>
      <td>Provoked</td>
      <td>one of the crew of the schooner Mary C. Brown</td>
      <td>Shooting sharks</td>
      <td>Survived, PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5455</th>
      <td>1890</td>
      <td>Provoked</td>
      <td>a charter fishing boat with James Whiteside an...</td>
      <td>Fishing for bluefish</td>
      <td>No injury to occupants. Hooked shark damaged b...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5475</th>
      <td>1889</td>
      <td>Provoked</td>
      <td>rowboat,</td>
      <td>Fishing</td>
      <td>No injury to occupants. Gaffed shark capsized ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5500</th>
      <td>1887</td>
      <td>Provoked</td>
      <td>boat</td>
      <td>NaN</td>
      <td>Harpooned shark, bit boat, causing it to ship ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5505</th>
      <td>1886</td>
      <td>Provoked</td>
      <td>Boat of Captain Forman White</td>
      <td>Netting menhaden, sharks caught in net</td>
      <td>No injury, sharks ripped net &amp; bit boat PROVOK...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5529</th>
      <td>1884</td>
      <td>Provoked</td>
      <td>child</td>
      <td>NaN</td>
      <td>FATAL            Leg severed by harpooned shar...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5536</th>
      <td>1883</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing for sharks</td>
      <td>Leg injured by hooked shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5544</th>
      <td>1882</td>
      <td>Provoked</td>
      <td>Mr. Hill</td>
      <td>Restraining a beached shark</td>
      <td>Hand severely nipped PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5581</th>
      <td>1879</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Fishing</td>
      <td>No injuries to occupants, Hooked shark bit boa...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5590</th>
      <td>1878</td>
      <td>Provoked</td>
      <td>Captain Pattison</td>
      <td>Fishing</td>
      <td>Leg bitten by netted shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5604</th>
      <td>1877</td>
      <td>Provoked</td>
      <td>John Smart</td>
      <td>NaN</td>
      <td>Fingers injured by landed shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5636</th>
      <td>1873</td>
      <td>Provoked</td>
      <td>James Green</td>
      <td>Fishing (Seining)</td>
      <td>Leg severely bitten by netted shark. Lower leg...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5649</th>
      <td>1871</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Shark fishing</td>
      <td>Hand injured PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5680</th>
      <td>1864</td>
      <td>Provoked</td>
      <td>fisherman</td>
      <td>Dragging a shark</td>
      <td>Knee bitten PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5743</th>
      <td>1852</td>
      <td>Provoked</td>
      <td>William Stannard</td>
      <td>Fishing</td>
      <td>Foot bitten by hooked shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5779</th>
      <td>1842</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Harassing a shark</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
    <tr>
      <th>5885</th>
      <td>0</td>
      <td>Provoked</td>
      <td>male</td>
      <td>NaN</td>
      <td>Cut to arm while roping shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Phillip Peters</td>
      <td>NaN</td>
      <td>Bitten by captive sharks PROVOKED INCIDENTS</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5914</th>
      <td>0</td>
      <td>Provoked</td>
      <td>a chief</td>
      <td>Attempting to drive shark from area</td>
      <td>Speared shark broke outrigger of canoe throwin...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5916</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Carl Bruster</td>
      <td>Skin diving. Grabbed shark's tail; shark turne...</td>
      <td>Ankle punctured &amp; lacerated, hands abraded PRO...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5940</th>
      <td>0</td>
      <td>Provoked</td>
      <td>John Fenton</td>
      <td>Testing movie camera in full diving dress</td>
      <td>Shark bit diver's sleeve after he patted it on...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5944</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Sandrillio</td>
      <td>Shark fishing, knocked overboard</td>
      <td>FATAL, hip bitten  PROVOKED INCIDENT</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>Carrying a supposedly dead shark by its mouth</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>557 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Stratton</td>
      <td>Fishing</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Ian Watkins</td>
      <td>Kayaking</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Raines</td>
      <td>Fishing in Alabama Deep Fishing Rodeo</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Mark Davis</td>
      <td>Fishing for squid</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2016</td>
      <td>Boat</td>
      <td>24' boat Shark Tagger Occupant Keith Poe</td>
      <td>Fishing for sharks</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>94</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Dev De Lange</td>
      <td>Kayak fishing</td>
      <td>No injury, shark capsized kayak</td>
      <td>N</td>
    </tr>
    <tr>
      <th>98</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupants: Hamza Humaid Al Sahra\92a &amp; 5 crew</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark leapt into boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Occupant: Grant Wardell</td>
      <td>Kayak Fishing</td>
      <td>No injury, kayak damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2015</td>
      <td>Boat</td>
      <td>6 m boat: occupants  Stephen &amp; Andrew Crust</td>
      <td>Fishing</td>
      <td>No injury, shark rammed boat &amp; bit motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>128</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Jordan Pavacich</td>
      <td>Kayak Fishing</td>
      <td>No injury, shark rammed kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>218</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Kayak: Occupant Kelly Janse van Rensburg</td>
      <td>Kayak Fishing</td>
      <td>No injury but kayak bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>222</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Dinghy: Occupant Robbie Graham</td>
      <td>Fishing</td>
      <td>Bruised in falling overboard as shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>225</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Avalon, a carbon kevlar monohull: 8 occupants</td>
      <td>Transatlantic Rowing</td>
      <td>No injury, shark bit rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>230</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Racing scull: Occupant Trevor Carter</td>
      <td>Rowing</td>
      <td>No injury, shark's teeth scratched hull</td>
      <td>N</td>
    </tr>
    <tr>
      <th>233</th>
      <td>2015</td>
      <td>Boat</td>
      <td>22-ft boat.  Occupant Captain Scott Fitzgerald</td>
      <td>Fishing</td>
      <td>No injury but shark bit trolling motor &amp; ramme...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>235</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Boat: occupants: Tim Watson &amp; Allan de Sylva</td>
      <td>Fishing</td>
      <td>Shark bumped boat, no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>252</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Boat: occupants: David Lock &amp; his father</td>
      <td>Fishing</td>
      <td>Shark chasing fish bumped boat, no injury to o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>254</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Boat: occupants: Matt Mitchell &amp; 2 other people</td>
      <td>NaN</td>
      <td>Shark bumped boat, no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>262</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Tara Burnley</td>
      <td>Canoeing</td>
      <td>No injury to occupant, canoe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>268</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Inflatable kayak Occupants:  Andrej Kultan &amp; S...</td>
      <td>Kayaking</td>
      <td>Kayak deflated, no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>271</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Ryan Howell</td>
      <td>Kayaking</td>
      <td>No injury to occupant, shark/s holded  kayak</td>
      <td>N</td>
    </tr>
    <tr>
      <th>272</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Raul Armenta</td>
      <td>Kayaking</td>
      <td>No injury to occupant, shark/s holded  kayak</td>
      <td>N</td>
    </tr>
    <tr>
      <th>316</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Victor Mooney</td>
      <td>Transatlantic Rowing</td>
      <td>His boat was holed by a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>343</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Inflatable boat</td>
      <td>Shark watching</td>
      <td>No injury to occupants, shark bit pontoon</td>
      <td>N</td>
    </tr>
    <tr>
      <th>359</th>
      <td>2014</td>
      <td>Boat</td>
      <td>OneDLL</td>
      <td>Sailing</td>
      <td>No injury to occupants, hull bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>366</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Dinghy. Occupants: Jeff Kurr and Andy Casagrande</td>
      <td>Filming a documentary</td>
      <td>No injury to occupants, shark nudged and bit boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>483</th>
      <td>2013</td>
      <td>Boat</td>
      <td>Occupants: Andrew &amp; Ben Donegan &amp; Joel Ryan,</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bit propeller</td>
      <td>N</td>
    </tr>
    <tr>
      <th>530</th>
      <td>2012</td>
      <td>Boat</td>
      <td>dinghy</td>
      <td>Fishing</td>
      <td>No injury, shark grabbed outboard motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>582</th>
      <td>2012</td>
      <td>Boat</td>
      <td>crayfish boat. Occupants: Dave &amp; Mitchell Dupe...</td>
      <td>Crayfishing</td>
      <td>No injury to occupants. Shark bit propelle, ro...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>595</th>
      <td>2012</td>
      <td>Boat</td>
      <td>8m inflatable boat. Occupants: Bhad Battle &amp; K...</td>
      <td>Fishing</td>
      <td>No injury to occupants, boat damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>3733</th>
      <td>1960</td>
      <td>Boat</td>
      <td>boat</td>
      <td>Fishing</td>
      <td>Shark rammed boat, breaching its hull</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3737</th>
      <td>1960</td>
      <td>Boat</td>
      <td>12' dinghy</td>
      <td>NaN</td>
      <td>No injury to occupants, toothmarks on bottom &amp;...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3780</th>
      <td>1960</td>
      <td>Boat</td>
      <td>5 m skiboat</td>
      <td>Fishing</td>
      <td>Shark rammed boat &amp; bit transom</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3793</th>
      <td>1960</td>
      <td>Boat</td>
      <td>13' dinghy, occupant S. Smith, Leenee Dee &amp; Ma...</td>
      <td>NaN</td>
      <td>No injury to occupants, shark lifted boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3796</th>
      <td>1960</td>
      <td>Boat</td>
      <td>16' boat, occupant: W. Lonergan</td>
      <td>Setting crayfish pots</td>
      <td>No injury to occupant, shark rammed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3808</th>
      <td>1959</td>
      <td>Boat</td>
      <td>12' ski, occupants: Bill Dyer &amp; Cliff Burgess</td>
      <td>Paddling</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3809</th>
      <td>1959</td>
      <td>Boat</td>
      <td>plywood dinghy, occupants: Jack Deegan &amp; Trevo...</td>
      <td>Fishing</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3815</th>
      <td>1959</td>
      <td>Boat</td>
      <td>dinghy, occupant: Don Ashton</td>
      <td>Fishing for snapper</td>
      <td>No injury to occupant, shark sank dinghy</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3821</th>
      <td>1959</td>
      <td>Boat</td>
      <td>boat Sea Hawk, occupants: R. Roberts &amp; 4 others</td>
      <td>Fishing for tunny</td>
      <td>R. Roberts' leg was bruised when shark leapt i...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3834</th>
      <td>1959</td>
      <td>Boat</td>
      <td>12' boat. Occupants:  Capt. E.J. Wines, Maj. W...</td>
      <td>Gigging for flounder</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3835</th>
      <td>1959</td>
      <td>Boat</td>
      <td>12 m fishing boat. Occupant: Henry Tervo</td>
      <td>Pulling hooked salmon to boat</td>
      <td>No injury to occupant, shark struck stern of boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3839</th>
      <td>1959</td>
      <td>Boat</td>
      <td>40' bonito boat</td>
      <td>Fishing</td>
      <td>No injury to occupants; shark bit rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3856</th>
      <td>1959</td>
      <td>Boat</td>
      <td>boat, occupant Robert Agnew</td>
      <td>NaN</td>
      <td>No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3857</th>
      <td>1959</td>
      <td>Boat</td>
      <td>15-foot boat: occupant Woodrow Smith</td>
      <td>Fishing</td>
      <td>No injury to occupant, shark rammed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3861</th>
      <td>1959</td>
      <td>Boat</td>
      <td>17' boat, occupant:  Richard Wade</td>
      <td>NaN</td>
      <td>No injury to occupant, shark bit propeller as ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3879</th>
      <td>1959</td>
      <td>Boat</td>
      <td>R.P. Straughan</td>
      <td>On boat, preparing to dive</td>
      <td>Boat followed shark; shark holed boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3880</th>
      <td>1959</td>
      <td>Boat</td>
      <td>14' open boat: occupants Richard Crew &amp; Bob Th...</td>
      <td>Fishing for snapper</td>
      <td>No injury to occupants. Shark leapt into boat,...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3901</th>
      <td>1958</td>
      <td>Boat</td>
      <td>Fishing boat. Occupants: Yunus Potur &amp; Ali Durmaz</td>
      <td>Fishing</td>
      <td>Boat damaged</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>3909</th>
      <td>1958</td>
      <td>Boat</td>
      <td>4.3 m skiff, occupant: Bob Shay</td>
      <td>Fishing</td>
      <td>No injury to occupant, shark chasing barracuda...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3917</th>
      <td>1958</td>
      <td>Boat</td>
      <td>16' cabin cruiser with 35 hp outboard motor</td>
      <td>Boat stopped to repair electric pump</td>
      <td>Shark tried to bite prop twice</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3953</th>
      <td>1958</td>
      <td>Boat</td>
      <td>ski-boat</td>
      <td>Fishing (trolling)</td>
      <td>No injury to occupants; shark bit propeller</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3962</th>
      <td>1957</td>
      <td>Boat</td>
      <td>16-foot launch, occupants: George Casey, Jack ...</td>
      <td>Fishing</td>
      <td>No injury, shark's teeth embedded in boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3988</th>
      <td>1957</td>
      <td>Boat</td>
      <td>boat, occupant: Portuondo</td>
      <td>Fishing</td>
      <td>No injury to occupant, shark stuck boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4016</th>
      <td>1956</td>
      <td>Boat</td>
      <td>boat:  occupants: Nazzareno Zammit &amp; Emmanuel</td>
      <td>Fishing</td>
      <td>No injury to occupants, but Emmanuel "later di...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5785</th>
      <td>1840</td>
      <td>Boat</td>
      <td>A dinghy</td>
      <td>Sailing</td>
      <td>No injury to occupant, shark seized stern post</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5830</th>
      <td>1804</td>
      <td>Boat</td>
      <td>boat</td>
      <td>NaN</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5834</th>
      <td>1788</td>
      <td>Boat</td>
      <td>boat</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bit oar and rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5839</th>
      <td>1776</td>
      <td>Boat</td>
      <td>Occupants of skin boats</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5902</th>
      <td>0</td>
      <td>Boat</td>
      <td>4.8-metre skiboat, Occupants: Rod Salm &amp; 4 fri...</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Boat</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>Wooden fishing boat</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>200 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>243</th>
      <td>2014</td>
      <td>Sea Disaster</td>
      <td>Passenger ferry Norman Atlantic</td>
      <td>NaN</td>
      <td>Of 9 bodies recovered, one was bitten by a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>365</th>
      <td>2014</td>
      <td>Sea Disaster</td>
      <td>Rianto</td>
      <td>Sea disaster</td>
      <td>5 cm bite to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>668</th>
      <td>2011</td>
      <td>Sea Disaster</td>
      <td>Fishing vessel. Occupants Gerry Malabago, Mark...</td>
      <td>Sea disaster</td>
      <td>The two Malabagos were bitten by sharks but su...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>935</th>
      <td>2009</td>
      <td>Sea Disaster</td>
      <td>occupant of a Cessna 206</td>
      <td>Air Disaster</td>
      <td>It is probable that all 5 passengers died on i...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>966</th>
      <td>2008</td>
      <td>Sea Disaster</td>
      <td>4 crew</td>
      <td>Sinking of the cargo ship Mark Jason</td>
      <td>Of the 20 crew, 4 were bitten by shark. None o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>969</th>
      <td>2008</td>
      <td>Sea Disaster</td>
      <td>Chen Te-hsing</td>
      <td>Fishing boat swamped in storm</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1032</th>
      <td>2008</td>
      <td>Sea Disaster</td>
      <td>unknown</td>
      <td>Sea Disaster</td>
      <td>Boat capsized in squall. 2 bodies scavenged  b...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1097</th>
      <td>2007</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>The 426-ton cargo ship Mia, laden with cement,...</td>
      <td>FATAL        Only 4 of the 18 on board were re...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1160</th>
      <td>2007</td>
      <td>Sea Disaster</td>
      <td>Haitian refugees perished when their boat caps...</td>
      <td>Sea Disaster</td>
      <td>Some of the bodies recovered had been bitten b...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1193</th>
      <td>2006</td>
      <td>Sea Disaster</td>
      <td>Sinking of the m.v.Leonida</td>
      <td>Sea Disaster</td>
      <td>15 perished but shark involvement prior to dea...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1219</th>
      <td>2006</td>
      <td>Sea Disaster</td>
      <td>a refugee</td>
      <td>Sea Disaster</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1366</th>
      <td>2005</td>
      <td>Sea Disaster</td>
      <td>Boat: 14' Sunfish. Occupants Josh Long &amp;  Troy...</td>
      <td>Sea Disaster</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1484</th>
      <td>2004</td>
      <td>Sea Disaster</td>
      <td>135 passengers &amp; 13 crew</td>
      <td>Air disaster. Flash Airlines Boeing 737 crashe...</td>
      <td>No survivors, sharks scavenged on remains</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1749</th>
      <td>2001</td>
      <td>Sea Disaster</td>
      <td>Unknown</td>
      <td>Sinking of the 40' Esperanza off St. Maartin w...</td>
      <td>Human remains recovered in shark caught off An...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1830</th>
      <td>2000</td>
      <td>Sea Disaster</td>
      <td>3 people</td>
      <td>Air Disaster - Piper aircraft crashed into the...</td>
      <td>Sharks prevented recovery of remains</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2093</th>
      <td>1996</td>
      <td>Sea Disaster</td>
      <td>No survivors. 189 people were lost</td>
      <td>Boeing 757 enroute from Porta Plata plunged in...</td>
      <td>106 bodies were recovered, some had been bitte...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2197</th>
      <td>1994</td>
      <td>Sea Disaster</td>
      <td>2 Cuban brothers</td>
      <td>Adrift on refugee raft</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2281</th>
      <td>1993</td>
      <td>Sea Disaster</td>
      <td>Haumole Faing'a</td>
      <td>Sea disaster</td>
      <td>Puncture wounds to right thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2282</th>
      <td>1993</td>
      <td>Sea Disaster</td>
      <td>Siale Sime</td>
      <td>Sea disaster</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2479</th>
      <td>1988</td>
      <td>Sea Disaster</td>
      <td>Bruce Coucom</td>
      <td>The Christie V sank on 11/6/1988, survivors we...</td>
      <td>FATAL  When James Coucom, the lone survivor, w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2480</th>
      <td>1988</td>
      <td>Sea Disaster</td>
      <td>Cedric Coucom</td>
      <td>The Christie V sank on 11/6/1988, survivors we...</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2481</th>
      <td>1988</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>The MV Dona Marilyn sank in Typhoon Unsang wit...</td>
      <td>According to survivors, many people were taken...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2533</th>
      <td>1987</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Ferry boat Dona Paz with 4431 passengers explo...</td>
      <td>25 people survived; 300 shark-mutilated bodies...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2541</th>
      <td>1987</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Vessel caught fire &amp; capsized, survivors in th...</td>
      <td>Of 160 people on board, &gt;100 missing</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2563</th>
      <td>1987</td>
      <td>Sea Disaster</td>
      <td>2 people</td>
      <td>The inter-island ferry Vula sank in heavy weather</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2690</th>
      <td>1983</td>
      <td>Sea Disaster</td>
      <td>Arturo Garces</td>
      <td>Ferry boat sank</td>
      <td>Left foot nipped</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2702</th>
      <td>1983</td>
      <td>Sea Disaster</td>
      <td>Linda Ann Norton</td>
      <td>Swimming from the New Venture</td>
      <td>FATAL, shark seized her by the chest and took ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2703</th>
      <td>1983</td>
      <td>Sea Disaster</td>
      <td>Dennis Patrick Murphy</td>
      <td>Swimming from the New Venture</td>
      <td>FATAL, shark bit leg, then dragged him underwa...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>2704</th>
      <td>1983</td>
      <td>Sea Disaster</td>
      <td>Ray Boundy</td>
      <td>14 m prawn trawler New Venture capsized  &amp; san...</td>
      <td>Left knee bitten, but survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2808</th>
      <td>1981</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Foundering of the Israeli freighter Mezada</td>
      <td>Next day 2 bodies recovered from sharks</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5501</th>
      <td>1887</td>
      <td>Sea Disaster</td>
      <td>Whittle</td>
      <td>The passenger ship Kapuna was run down the ore...</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5503</th>
      <td>1887</td>
      <td>Sea Disaster</td>
      <td>a ship's steward</td>
      <td>British ship Macedon was thrown on her beam en...</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5522</th>
      <td>1885</td>
      <td>Sea Disaster</td>
      <td>sailor</td>
      <td>Wreck of the schooner Pohoiki</td>
      <td>Left arm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5523</th>
      <td>1885</td>
      <td>Sea Disaster</td>
      <td>sailor</td>
      <td>Wreck of the schooner Pohoiki</td>
      <td>Laceration to torso</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5524</th>
      <td>1885</td>
      <td>Sea Disaster</td>
      <td>Captain Mark Robinson</td>
      <td>Wreck of the schooner Pohoiki</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5528</th>
      <td>1884</td>
      <td>Sea Disaster</td>
      <td>Willaim Browne</td>
      <td>yachting accident</td>
      <td>Cause of death most likely drowning, remains r...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5565</th>
      <td>1880</td>
      <td>Sea Disaster</td>
      <td>The Lamont Young party</td>
      <td>Traveling by boat</td>
      <td>Disappeared, thought to have murdered or drown...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5582</th>
      <td>1879</td>
      <td>Sea Disaster</td>
      <td>male + 20</td>
      <td>NaN</td>
      <td>Severely bitten on heel, 20 others taken by sh...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5591</th>
      <td>1878</td>
      <td>Sea Disaster</td>
      <td>Antonio du Val</td>
      <td>Boat with 5 men capsized while returning to th...</td>
      <td>Du Val's leg was bitten but he survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5592</th>
      <td>1878</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Boat with 5 men capsized while returning to th...</td>
      <td>FATAL, 2 of the crew were killed by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5597</th>
      <td>1878</td>
      <td>Sea Disaster</td>
      <td>An Arab who had been with Stanley when he met ...</td>
      <td>Wreck of the Union Steamship Company 982-ton i...</td>
      <td>FATAL, shark removed large part of his hip</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5599</th>
      <td>1877</td>
      <td>Sea Disaster</td>
      <td>a male &amp; a female</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5644</th>
      <td>1872</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Wreck of the 150-ton brig Maria</td>
      <td>FATAL, some were taken by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5646</th>
      <td>1872</td>
      <td>Sea Disaster</td>
      <td>an Italian fisherman</td>
      <td>Adrift on a raft</td>
      <td>Leg bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5667</th>
      <td>1868</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>A junk foundered</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5668</th>
      <td>1868</td>
      <td>Sea Disaster</td>
      <td>boat, occupants: John Griffiths &amp; Thomas Johnson</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark's teeth embedded...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5673</th>
      <td>1867</td>
      <td>Sea Disaster</td>
      <td>2 crew clinging to floating barrels</td>
      <td>boat from ship Josephine capsized in squall</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5716</th>
      <td>1860</td>
      <td>Sea Disaster</td>
      <td>a Cook's Islander</td>
      <td>43-ton schooner Irene capsized &amp; sank</td>
      <td>Probable drowning</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5728</th>
      <td>1855</td>
      <td>Sea Disaster</td>
      <td>sailor</td>
      <td>ship William Penn grounded &amp; broke apart</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5749</th>
      <td>1852</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Wreck of the steamship Birkenhead</td>
      <td>FATAL. All of the women &amp; children on board su...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5766</th>
      <td>1847</td>
      <td>Sea Disaster</td>
      <td>Spicer</td>
      <td>Wreck of the Sovereign</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5770</th>
      <td>1846</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Wreck of the USS Somers</td>
      <td>FATAL, some were taken by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5806</th>
      <td>1829</td>
      <td>Sea Disaster</td>
      <td>Ned &amp; Pawn</td>
      <td>Wreck of the schooner Driver</td>
      <td>FATAL x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5815</th>
      <td>1826</td>
      <td>Sea Disaster</td>
      <td>Lieutenant Edward Smith</td>
      <td>HBM Magpie foundered in a squall</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5870</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Shipwrecked Persian Fleet</td>
      <td>Herodotus tells of sharks attacking men in the...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5871</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Vase depicts shipwrecked sailors, one of whom ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>C.</td>
      <td>A group of survivors on a raft for 17-days</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>pilot</td>
      <td>Spent 8 days in dinghy</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>male</td>
      <td>Aircraft ditched in the sea, swimming ashore</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>220 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Jack O'Neill</td>
      <td>Surfing</td>
      <td>No injury, board damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>73</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>a British citizen</td>
      <td>NaN</td>
      <td>"Serious"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>75</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Maximo Trinidad</td>
      <td>SUP</td>
      <td>Fell off board when spinner shark leapt from t...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>81</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>unknown</td>
      <td>Surfing</td>
      <td>Board reportedly bumped by shark. No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>90</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Richard Branson</td>
      <td>Feeding stingrays?</td>
      <td>Minor injury to wrist from Southern stingray</td>
      <td>N</td>
    </tr>
    <tr>
      <th>91</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Surfing</td>
      <td>No injury, knocked off board</td>
      <td>N</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Ryla Underwood</td>
      <td>Surfing</td>
      <td>Lower left leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>126</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Left foot bitten by eel</td>
      <td>N</td>
    </tr>
    <tr>
      <th>154</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>young boy</td>
      <td>NaN</td>
      <td>Wound to right lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>159</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Minor injury when he attempted to touch a fish.</td>
      <td>N</td>
    </tr>
    <tr>
      <th>163</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>female</td>
      <td>Floating</td>
      <td>2' cut to dorsum of foot, 2 puncture wounds to...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>170</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugene Finney</td>
      <td>Treading water</td>
      <td>Laceration to back</td>
      <td>N</td>
    </tr>
    <tr>
      <th>171</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Joe Termini</td>
      <td>Swimming</td>
      <td>Parallel lacerations to torso inconsistent wit...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>181</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>female</td>
      <td>Swimming</td>
      <td>Minor lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>187</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Lily Kumpe</td>
      <td>Surfing</td>
      <td>Bruises and abrasions to face, chin, chest, bo...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>215</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Diego Gomes Mota</td>
      <td>Surfing</td>
      <td>Injury to left thigh from unidentified species...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugenio Masala</td>
      <td>Diving</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>234</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Diane Ellis</td>
      <td>Surfing &amp; filming dolphins</td>
      <td>Board snapped in two</td>
      <td>N</td>
    </tr>
    <tr>
      <th>237</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Rob Konrad</td>
      <td>Swimming after falling overboard</td>
      <td>During his 16-hour swim to shore, he was circl...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>244</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>5 people claimed to have been injured by a "ba...</td>
      <td>Swimming</td>
      <td>Minor cuts on feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>277</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Beau Browning</td>
      <td>Surfing</td>
      <td>A hoax, no shark involvement</td>
      <td>N</td>
    </tr>
    <tr>
      <th>285</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>child</td>
      <td>NaN</td>
      <td>Shark involvement not confirmed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>303</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Cuban refugees</td>
      <td>Sea disaster</td>
      <td>Shark involvement prior to death not confirmed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>John Petty</td>
      <td>Shark diving</td>
      <td>Missing after a dive, shark involvement consid...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Jimmy Roseman</td>
      <td>Diving</td>
      <td>No injury. No attack. 12' white shark appeared...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>348</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Michael McGregor</td>
      <td>Diving for lobsters</td>
      <td>Shark bites may have been post mortem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>354</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Jason Dimitri</td>
      <td>Scuba diving / culling lionfish</td>
      <td>Caribbean reef shark buzzed him. No injury, no...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>355</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Myxie Ryan</td>
      <td>NaN</td>
      <td>Injuries to wrist/hand by a mackerel, not a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>410</th>
      <td>2013</td>
      <td>Invalid</td>
      <td>Charlotte Brynn</td>
      <td>Marathon swimming</td>
      <td>Puncture wound to torso. Reported as a bite by...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>434</th>
      <td>2013</td>
      <td>Invalid</td>
      <td>Thierry Frennet</td>
      <td>Swimming</td>
      <td>Scrape to right forearm. Frennet says inflicte...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5645</th>
      <td>1872</td>
      <td>Invalid</td>
      <td>Mr. Manning</td>
      <td>boat capsized</td>
      <td>Probable drowning</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5647</th>
      <td>1871</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Human remains recovered from 11' shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5662</th>
      <td>1870</td>
      <td>Invalid</td>
      <td>Sub Lieut. Bowyer of H.M.S. Chile</td>
      <td>Canoeing</td>
      <td>Shark bit canoe in half &amp; bit man. Note: There...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5664</th>
      <td>1869</td>
      <td>Invalid</td>
      <td>Christian Frederick</td>
      <td>Fell overboard</td>
      <td>FATAL, but shark involvement prior to death wa...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5675</th>
      <td>1866</td>
      <td>Invalid</td>
      <td>Mr. Groves</td>
      <td>Fell overboard</td>
      <td>Thought to have been taken by a shark. Body wa...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5687</th>
      <td>1864</td>
      <td>Invalid</td>
      <td>Mr. Warren, Jr.</td>
      <td>Swimming</td>
      <td>Presumed Fatal, but shark involvement not conf...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5692</th>
      <td>1863</td>
      <td>Invalid</td>
      <td>Mr. J. Canham</td>
      <td>Swimming, caught in strong backwash &amp; disappeared</td>
      <td>Shark caught 9 days later contained human rema...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5699</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Possible drowning and scavenging</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5719</th>
      <td>1858</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Thought to have been taken by a shark/s. Body ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5720</th>
      <td>1858</td>
      <td>Invalid</td>
      <td>3 males</td>
      <td>Swimming</td>
      <td>Thought to have been taken by a shark/s. Bodie...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5733</th>
      <td>1855</td>
      <td>Invalid</td>
      <td>C.T. Clark</td>
      <td>Swimming</td>
      <td>No injury &amp; although reported as an attack, it...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5740</th>
      <td>1853</td>
      <td>Invalid</td>
      <td>a young man</td>
      <td>He was fighting a shark when his boat capsized...</td>
      <td>His gold watch was later found in a shark but...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5742</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Edward Graham</td>
      <td>Swimming</td>
      <td>Shark involvement prior to death was not confi...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>NaN</td>
      <td>Death preceded shark involvement</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5761</th>
      <td>1849</td>
      <td>Invalid</td>
      <td>William Henry Elliott</td>
      <td>boat capsized</td>
      <td>Torso bitten but may have been postmorem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5768</th>
      <td>1847</td>
      <td>Invalid</td>
      <td>a young sailor</td>
      <td>Swimming</td>
      <td>Disappeared, thought to have been taken by a s...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5787</th>
      <td>1839</td>
      <td>Invalid</td>
      <td>Mr.Johnson (male)</td>
      <td>NaN</td>
      <td>"Drowned, 2 days later his head was bitten off...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5793</th>
      <td>1837</td>
      <td>Invalid</td>
      <td>adult male, a sailor</td>
      <td>NaN</td>
      <td>Shark caught contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shark caught, contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5801</th>
      <td>1831</td>
      <td>Invalid</td>
      <td>Robert Dudlow</td>
      <td>Boat capsized, clinging to line</td>
      <td>Drowned, no shark involvement</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5817</th>
      <td>1825</td>
      <td>Invalid</td>
      <td>Nelson</td>
      <td>NaN</td>
      <td>Arms severed, but he survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5819</th>
      <td>1819</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>No injury / No attack</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5820</th>
      <td>1818</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Probable drowning</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5829</th>
      <td>1805</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>human remains (male) found in shark\92s gut</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5841</th>
      <td>1767</td>
      <td>Invalid</td>
      <td>Samuel Matthews</td>
      <td>Bathing</td>
      <td>Lacerations to arm &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5855</th>
      <td>1642</td>
      <td>Invalid</td>
      <td>crew member of the Nieuwstadt</td>
      <td>Went overboard</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5917</th>
      <td>0</td>
      <td>Invalid</td>
      <td>Dan Hogan</td>
      <td>Scuba diving</td>
      <td>Said to be fatal but incident highly questionable</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5922</th>
      <td>0</td>
      <td>Invalid</td>
      <td>Val Valentine</td>
      <td>Diving</td>
      <td>A 4.3 m [14'] shark made threat display. No in...</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>519 rows × 6 columns</p>
</div>



```python
#Analisis del atributo 'Sex '
display(df6.loc[df6['Sex ']=='N',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='.',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='lli',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='Nulos',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Sex ']=='F',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='M',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='M ',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
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
      <th>Type</th>
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
      <td>Boating</td>
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
      <th>Type</th>
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
      <td>Sea Disaster</td>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
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
      <th>Type</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Stratton</td>
      <td>Nulos</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Raines</td>
      <td>Nulos</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>81</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>unknown</td>
      <td>Nulos</td>
      <td>Board reportedly bumped by shark. No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2015</td>
      <td>Boat</td>
      <td>6 m boat: occupants  Stephen &amp; Andrew Crust</td>
      <td>Nulos</td>
      <td>No injury, shark rammed boat &amp; bit motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>225</th>
      <td>2015</td>
      <td>Boat</td>
      <td>Avalon, a carbon kevlar monohull: 8 occupants</td>
      <td>Nulos</td>
      <td>No injury, shark bit rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>241</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Jeff Brown</td>
      <td>Nulos</td>
      <td>Lacerations to both feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>243</th>
      <td>2014</td>
      <td>Sea Disaster</td>
      <td>Passenger ferry Norman Atlantic</td>
      <td>Nulos</td>
      <td>Of 9 bodies recovered, one was bitten by a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>244</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>5 people claimed to have been injured by a "ba...</td>
      <td>Nulos</td>
      <td>Minor cuts on feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>254</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Boat: occupants: Matt Mitchell &amp; 2 other people</td>
      <td>Nulos</td>
      <td>Shark bumped boat, no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>285</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>child</td>
      <td>Nulos</td>
      <td>Shark involvement not confirmed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>291</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Miller Diggs</td>
      <td>Nulos</td>
      <td>Laceration to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>307</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>child</td>
      <td>Nulos</td>
      <td>Minor injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>343</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Inflatable boat</td>
      <td>Nulos</td>
      <td>No injury to occupants, shark bit pontoon</td>
      <td>N</td>
    </tr>
    <tr>
      <th>366</th>
      <td>2014</td>
      <td>Boat</td>
      <td>Dinghy. Occupants: Jeff Kurr and Andy Casagrande</td>
      <td>Nulos</td>
      <td>No injury to occupants, shark nudged and bit boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>478</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Lacerations to right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>517</th>
      <td>2012</td>
      <td>Unprovoked</td>
      <td>teen</td>
      <td>Nulos</td>
      <td>Minor injury to elbow</td>
      <td>N</td>
    </tr>
    <tr>
      <th>524</th>
      <td>2012</td>
      <td>Provoked</td>
      <td>M. Malabon</td>
      <td>Nulos</td>
      <td>Minor laceration to hand  PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>530</th>
      <td>2012</td>
      <td>Boat</td>
      <td>dinghy</td>
      <td>Nulos</td>
      <td>No injury, shark grabbed outboard motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>548</th>
      <td>2012</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Leg struck. Initally reported as a shark attac...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>582</th>
      <td>2012</td>
      <td>Boat</td>
      <td>crayfish boat. Occupants: Dave &amp; Mitchell Dupe...</td>
      <td>Nulos</td>
      <td>No injury to occupants. Shark bit propelle, ro...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>595</th>
      <td>2012</td>
      <td>Boat</td>
      <td>8m inflatable boat. Occupants: Bhad Battle &amp; K...</td>
      <td>Nulos</td>
      <td>No injury to occupants, boat damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>598</th>
      <td>2012</td>
      <td>Unprovoked</td>
      <td>J. Graden</td>
      <td>Nulos</td>
      <td>No injury, shark bit swim fin</td>
      <td>N</td>
    </tr>
    <tr>
      <th>616</th>
      <td>2011</td>
      <td>Invalid</td>
      <td>Dave Fordson</td>
      <td>Nulos</td>
      <td>Killed by a shark or crocodile.</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>626</th>
      <td>2011</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Arm bitten by captive shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>647</th>
      <td>2011</td>
      <td>Unprovoked</td>
      <td>M. Filipe</td>
      <td>Nulos</td>
      <td>No injury, shark bit surfboard</td>
      <td>N</td>
    </tr>
    <tr>
      <th>688</th>
      <td>2011</td>
      <td>Boat</td>
      <td>16' Dreamcatcher. Occupant: Ian Bussus</td>
      <td>Nulos</td>
      <td>No injury, shark slammed into boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>733</th>
      <td>2011</td>
      <td>Boat</td>
      <td>A 'tinnie". Occupants :Paul Sweeny, Paul Nieuw...</td>
      <td>Nulos</td>
      <td>No injury, shark nudged boat and bit propeller</td>
      <td>N</td>
    </tr>
    <tr>
      <th>844</th>
      <td>2009</td>
      <td>Boat</td>
      <td>Surf boat with 5 lifesavers on board</td>
      <td>Nulos</td>
      <td>No injury to occupants; shark bit steering oar</td>
      <td>N</td>
    </tr>
    <tr>
      <th>941</th>
      <td>2009</td>
      <td>Boat</td>
      <td>7.2 m boat. Occupant Kelvin Travers</td>
      <td>Nulos</td>
      <td>No injury to occupant, shark removed small aux...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>947</th>
      <td>2009</td>
      <td>Unprovoked</td>
      <td>4 poachers</td>
      <td>Nulos</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5628</th>
      <td>1874</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Shark and boat collided. No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5635</th>
      <td>1874</td>
      <td>Boating</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>2 people out of +70 survived, one of whom was ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5644</th>
      <td>1872</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>FATAL, some were taken by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5668</th>
      <td>1868</td>
      <td>Sea Disaster</td>
      <td>boat, occupants: John Griffiths &amp; Thomas Johnson</td>
      <td>Nulos</td>
      <td>No injury to occupants, shark's teeth embedded...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5679</th>
      <td>1865</td>
      <td>Boating</td>
      <td>R.H. Barrett, pilot holding steering oar of wh...</td>
      <td>Nulos</td>
      <td>No injury to pilot, oar bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5767</th>
      <td>1847</td>
      <td>Unprovoked</td>
      <td>a native</td>
      <td>Nulos</td>
      <td>Foot severed at ankle joint</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5779</th>
      <td>1842</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Nulos</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
    <tr>
      <th>5785</th>
      <td>1840</td>
      <td>Boat</td>
      <td>A dinghy</td>
      <td>Nulos</td>
      <td>No injury to occupant, shark seized stern post</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Shark caught, contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5795</th>
      <td>1836</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>No details, it was the year the first settlers...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5818</th>
      <td>1822</td>
      <td>Unprovoked</td>
      <td>slaves</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5825</th>
      <td>1816</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5830</th>
      <td>1804</td>
      <td>Boat</td>
      <td>boat</td>
      <td>Nulos</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5834</th>
      <td>1788</td>
      <td>Boat</td>
      <td>boat</td>
      <td>Nulos</td>
      <td>No injury to occupants, shark bit oar and rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5839</th>
      <td>1776</td>
      <td>Boat</td>
      <td>Occupants of skin boats</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5857</th>
      <td>1637</td>
      <td>Unprovoked</td>
      <td>Hindu pilgrims</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5858</th>
      <td>1617</td>
      <td>Unprovoked</td>
      <td>Indian people</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5865</th>
      <td>500</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Nulos</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5871</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Vase depicts shipwrecked sailors, one of whom ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5875</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Injury required 16 stitches</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5892</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Passenger &amp; crew</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5902</th>
      <td>0</td>
      <td>Boat</td>
      <td>4.8-metre skiboat, Occupants: Rod Salm &amp; 4 fri...</td>
      <td>Nulos</td>
      <td>No injury to occupants, shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5909</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Albert Raiti</td>
      <td>Nulos</td>
      <td>Lacerations to hands and knee</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5927</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>C.</td>
      <td>Nulos</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>Nulos</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>567 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to toes</td>
      <td>N</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>5 tiny puncture marks to lower leg, treated wi...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Buttocks, thigh, left hand &amp; wrist injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Marin Alice Melton</td>
      <td>F</td>
      <td>Injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>57</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Maria Korcsmaros \n</td>
      <td>F</td>
      <td>Injuries to arm and shoulder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>59</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Mary Marcus</td>
      <td>F</td>
      <td>Puncture wounds to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>60</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Krystal Magee</td>
      <td>F</td>
      <td>Lacerations and puncture wounds to foot and ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>61</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Back, arm &amp; hand injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>female</td>
      <td>F</td>
      <td>Arm grabbed PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>J. Orr</td>
      <td>F</td>
      <td>Minor injury to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>89</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Patricia Howe</td>
      <td>F</td>
      <td>Avulsion injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Foot nipped</td>
      <td>N</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Kaya Waldman</td>
      <td>F</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Cristina Ojeda-Thies</td>
      <td>F</td>
      <td>Lacerations to left forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>111</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Tamsin Scott</td>
      <td>F</td>
      <td>Lacerations to both hands and forearms</td>
      <td>N</td>
    </tr>
    <tr>
      <th>113</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Ryla Underwood</td>
      <td>F</td>
      <td>Lower left leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>118</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Jill Kruse</td>
      <td>F</td>
      <td>Injury to right ankle/calf &amp; hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>129</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Meti Kershner</td>
      <td>F</td>
      <td>Laceration to forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>137</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Laceration to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>146</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Caterina Gennaro</td>
      <td>F</td>
      <td>No injury, shark struck board, tossing her int...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>150</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Jane Neame</td>
      <td>F</td>
      <td>Left foot &amp; ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>152</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Elinor Dempsey</td>
      <td>F</td>
      <td>No injury, surfboard bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>157</th>
      <td>2015</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5435</th>
      <td>1892</td>
      <td>Unprovoked</td>
      <td>Mrs. Coe</td>
      <td>F</td>
      <td>Abrasions to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5508</th>
      <td>1886</td>
      <td>Invalid</td>
      <td>2 women</td>
      <td>F</td>
      <td>The body of one woman had been bitten by a sha...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5529</th>
      <td>1884</td>
      <td>Provoked</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL            Leg severed by harpooned shar...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5533</th>
      <td>1884</td>
      <td>Unprovoked</td>
      <td>Miss Warren</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5569</th>
      <td>1880</td>
      <td>Unprovoked</td>
      <td>a widow</td>
      <td>F</td>
      <td>Hands, forearm &amp; left thigh lacerated, radial ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5574</th>
      <td>1880</td>
      <td>Unprovoked</td>
      <td>Teresa Bonnell</td>
      <td>F</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5595</th>
      <td>1878</td>
      <td>Unprovoked</td>
      <td>Dolores Margarita Corrales y Roa</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5610</th>
      <td>1877</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Ankle injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5698</th>
      <td>1862</td>
      <td>Unprovoked</td>
      <td>The widowed Marchioness of Lendinez</td>
      <td>F</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5705</th>
      <td>1862</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5730</th>
      <td>1855</td>
      <td>Unprovoked</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>F</td>
      <td>Death preceded shark involvement</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5760</th>
      <td>1849</td>
      <td>Unprovoked</td>
      <td>Mrs. Cracton</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5798</th>
      <td>1834</td>
      <td>Unprovoked</td>
      <td>Kaugatava Orurutm</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5799</th>
      <td>1832</td>
      <td>Unprovoked</td>
      <td>Aboriginal female</td>
      <td>F</td>
      <td>Leg severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5832</th>
      <td>1800</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>F</td>
      <td>FATAL, all onboard were killed by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5833</th>
      <td>1791</td>
      <td>Unprovoked</td>
      <td>female, an Australian aboriginal</td>
      <td>F</td>
      <td>FATAL, "bitten in two"</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5879</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Lassie</td>
      <td>F</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5883</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Martha Hatagouei</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Leg severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Danniell Washington</td>
      <td>F</td>
      <td>Severe abrasion to forearm from captive shark ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5896</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Sametra Mestri</td>
      <td>F</td>
      <td>Hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5910</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female, a Hae Nyeo</td>
      <td>F</td>
      <td>FATAL, injured while diving, then shark bit her</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5913</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5918</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jill Reed</td>
      <td>F</td>
      <td>Shoulder scratched, swim fin bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5921</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>woman</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>585 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Puncture wounds to foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Michael Dornellas</td>
      <td>M</td>
      <td>Face bruised when partly blind shark collided ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Mark Davis</td>
      <td>M</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2016</td>
      <td>Provoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Boat</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4835 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Laceration &amp; puncture wounds to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1363</th>
      <td>2005</td>
      <td>Unprovoked</td>
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
display(df6.loc[df6['Fatal (Y/N)']=='UNKNOWN',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='#VALUE!',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='F',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='Nulos',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])

display(df6.loc[df6['Fatal (Y/N)']=='Y',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='N',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='N ',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']==' N',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='n',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1047</th>
      <td>2008</td>
      <td>Unprovoked</td>
      <td>Jamie Adlington</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1142</th>
      <td>2007</td>
      <td>Invalid</td>
      <td>Alex Takyi</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2025</th>
      <td>1997</td>
      <td>Unprovoked</td>
      <td>Jos\E9 Luiz Lipiani</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2035</th>
      <td>1997</td>
      <td>Unprovoked</td>
      <td>Gersome Perreno</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2042</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Blair Hall</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2070</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Trimurti Day</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2082</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Wayne Leong</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2098</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Marris</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2103</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>Carlton Taniyama</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2163</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>Hutchins</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2179</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2184</th>
      <td>1994</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2317</th>
      <td>1992</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2423</th>
      <td>1990</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2425</th>
      <td>1989</td>
      <td>Unprovoked</td>
      <td>Ryan Johnson</td>
      <td>M</td>
      <td>No details, "recovering in Darwin Hospital"</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2436</th>
      <td>1989</td>
      <td>Unprovoked</td>
      <td>John Benson</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2581</th>
      <td>1986</td>
      <td>Unprovoked</td>
      <td>Crawford</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2657</th>
      <td>1984</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2675</th>
      <td>1984</td>
      <td>Unprovoked</td>
      <td>Greenwood</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2718</th>
      <td>1983</td>
      <td>Unprovoked</td>
      <td>Arnold Schwarzwood</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2771</th>
      <td>1982</td>
      <td>Boat</td>
      <td>Giovanni Vuoso</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2773</th>
      <td>1982</td>
      <td>Unprovoked</td>
      <td>English holiday-maker</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2781</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>Robert Conklin</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2813</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2816</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>Filmer</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2982</th>
      <td>1975</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3073</th>
      <td>1973</td>
      <td>Unprovoked</td>
      <td>G. Cole</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3171</th>
      <td>1970</td>
      <td>Unprovoked</td>
      <td>David Vota</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3186</th>
      <td>1970</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>4977</th>
      <td>1923</td>
      <td>Invalid</td>
      <td>John Hayes</td>
      <td>M</td>
      <td>Death may have been due to drowning</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4987</th>
      <td>1922</td>
      <td>Invalid</td>
      <td>H.R.W.</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5014</th>
      <td>1921</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Buttons &amp; shoes found in shark caught in fish ...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5038</th>
      <td>1919</td>
      <td>Invalid</td>
      <td>5 cadets from the Naval training ship Tingara</td>
      <td>M</td>
      <td>Shark involvement not confirmed</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5097</th>
      <td>1915</td>
      <td>Invalid</td>
      <td>Remains of male found in shark</td>
      <td>M</td>
      <td>Fatal, drowning or scavenging</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5114</th>
      <td>1914</td>
      <td>Unprovoked</td>
      <td>Indian female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5120</th>
      <td>1913</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>M</td>
      <td>Man's leg recovered from 800-lb shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5121</th>
      <td>1913</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>F</td>
      <td>Female foot recovered from shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5134</th>
      <td>1912</td>
      <td>Invalid</td>
      <td>arm recovered from hooked shark</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5173</th>
      <td>1910</td>
      <td>Unprovoked</td>
      <td>Lieut. James H. Stewart</td>
      <td>M</td>
      <td>Calf removed, not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5308</th>
      <td>1901</td>
      <td>Invalid</td>
      <td>boy</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5316</th>
      <td>1900</td>
      <td>Unprovoked</td>
      <td>George Brown</td>
      <td>M</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5355</th>
      <td>1898</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Unknown</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5373</th>
      <td>1897</td>
      <td>Unprovoked</td>
      <td>Anonymous</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5411</th>
      <td>1894</td>
      <td>Unprovoked</td>
      <td>Catherine Beach</td>
      <td>F</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5414</th>
      <td>1894</td>
      <td>Unprovoked</td>
      <td>Erskine H. Reynolds</td>
      <td>M</td>
      <td>"Painfully injured" but no details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5432</th>
      <td>1893</td>
      <td>Unprovoked</td>
      <td>No details</td>
      <td>Nulos</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5464</th>
      <td>1890</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5465</th>
      <td>1890</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5726</th>
      <td>1856</td>
      <td>Unprovoked</td>
      <td>a seaman from the John and Lucy</td>
      <td>M</td>
      <td>Severe bite to thigh. Not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5795</th>
      <td>1836</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>No details, it was the year the first settlers...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5845</th>
      <td>1755</td>
      <td>Unprovoked</td>
      <td>Fishermen</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5856</th>
      <td>1638</td>
      <td>Unprovoked</td>
      <td>sailors</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5857</th>
      <td>1637</td>
      <td>Unprovoked</td>
      <td>Hindu pilgrims</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5858</th>
      <td>1617</td>
      <td>Unprovoked</td>
      <td>Indian people</td>
      <td>Nulos</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5860</th>
      <td>1595</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Leg severed mid-thigh, hand severed, arm above...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5862</th>
      <td>1555</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5863</th>
      <td>1554</td>
      <td>Unprovoked</td>
      <td>males (wearing armor)</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
  </tbody>
</table>
<p>94 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Invalid</td>
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
      <th>Type</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4693</th>
      <td>1935</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>human remains washed ahore</td>
      <td>F</td>
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
      <th>Type</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Waade Madigan and Dr Seyong Kim</td>
      <td>M</td>
      <td>No injury, but sharks repeatedly hit their fin...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>1844</th>
      <td>2000</td>
      <td>Invalid</td>
      <td>Ricky Stringer</td>
      <td>M</td>
      <td>Reported as shark attack but probable drowning</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>2449</th>
      <td>1969</td>
      <td>Invalid</td>
      <td>Russian male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>3280</th>
      <td>1967</td>
      <td>Provoked</td>
      <td>Romeo Guarini</td>
      <td>M</td>
      <td>Diver shot the shark, then it injured his arm ...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>3435</th>
      <td>1964</td>
      <td>Invalid</td>
      <td>Giancarlo Griffon</td>
      <td>M</td>
      <td>Disappeared, probable drowning but sharks in a...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>3901</th>
      <td>1958</td>
      <td>Boat</td>
      <td>Fishing boat. Occupants: Yunus Potur &amp; Ali Durmaz</td>
      <td>Nulos</td>
      <td>Boat damaged</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>4107</th>
      <td>1954</td>
      <td>Boating</td>
      <td>10 crew</td>
      <td>M</td>
      <td>No injury to occupants. Shark tore nets &amp; traw...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>4112</th>
      <td>1954</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Nulos</td>
      <td>Human remains found in shark</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5307</th>
      <td>1901</td>
      <td>Invalid</td>
      <td>Antonio Tornatori</td>
      <td>M</td>
      <td>Disappeared, but shark involvement unconfirmed</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5437</th>
      <td>1892</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>No injury, no attack</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5468</th>
      <td>1889</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Human remains found in 4m, 900 kg shark</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5642</th>
      <td>1872</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>No injury</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5699</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Possible drowning and scavenging</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5718</th>
      <td>1859</td>
      <td>Unprovoked</td>
      <td>J.G. Luther</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>F</td>
      <td>Death preceded shark involvement</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5793</th>
      <td>1837</td>
      <td>Invalid</td>
      <td>adult male, a sailor</td>
      <td>M</td>
      <td>Shark caught contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Shark caught, contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5820</th>
      <td>1818</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Probable drowning</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>Nulos</td>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>56</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Ben Gerring</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>83</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Maika Tabua</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>108</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Adrian Esteban Rafael</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>164</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Damien Johnson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Yves Berthelot</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>208</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Margaret Cruse</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Elio Canestri</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugenio Masala</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>219</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>226</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Talon Bishop</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>227</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Tadashi Nakahara</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>242</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Jay Muscat</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>248</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Daniel Smith</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>251</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Rameshwar Ram Dhauro</td>
      <td>M</td>
      <td>FATAL, arm bitten by shark hauled on deck     ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>278</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Paul Wilcox</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>303</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Cuban refugees</td>
      <td>M</td>
      <td>Shark involvement prior to death not confirmed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>John Petty</td>
      <td>M</td>
      <td>Missing after a dive, shark involvement consid...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>347</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Christine Armstrong</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>348</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Michael McGregor</td>
      <td>M</td>
      <td>Shark bites may have been post mortem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>349</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Friedrich Burgstaller.</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>360</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Sam Kellett</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>373</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Patrick Briney</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>374</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Zac Young</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>376</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Chris Boyd</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>390</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Burgert Van Der Westhuizen</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>416</th>
      <td>2013</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5942</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5943</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>an Indian</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5944</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Sandrillio</td>
      <td>M</td>
      <td>FATAL, hip bitten  PROVOKED INCIDENT</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5948</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Gilbertese fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>C.</td>
      <td>Nulos</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5952</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>an old fisherman</td>
      <td>M</td>
      <td>FATAL, foot lacerated &amp; crushed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5953</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a local dignitary</td>
      <td>M</td>
      <td>FATAL, femoral artery severed, died 12 days la...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5954</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>I.A.S. C. driver</td>
      <td>M</td>
      <td>FATAL, fell into water when shark seized his r...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5955</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL, left leg bitten with severe blood loss</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5956</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>FATAL, died of sepsis</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Nulos</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>Nulos</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>1552 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Stratton</td>
      <td>Nulos</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Boat</td>
      <td>Occupant: Ben Raines</td>
      <td>Nulos</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5928</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Dalton Baldwin</td>
      <td>M</td>
      <td>No injury, bumped by shark which took speared ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5929</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Les Bishop</td>
      <td>M</td>
      <td>Bumped by sharks</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5931</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Right hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5932</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Arm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5933</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Right leg lacerated &amp; surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5934</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, a sponge Diver</td>
      <td>M</td>
      <td>Lower leg and forearm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5936</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ross Doe</td>
      <td>M</td>
      <td>Shoulder abraded by skin of shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5939</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Horton Chase</td>
      <td>M</td>
      <td>Abrasions &amp; bruises hip to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5940</th>
      <td>0</td>
      <td>Provoked</td>
      <td>John Fenton</td>
      <td>M</td>
      <td>Shark bit diver's sleeve after he patted it on...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5945</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5946</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Dusty Rhodes</td>
      <td>M</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5947</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5950</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>American male</td>
      <td>M</td>
      <td>Buttock bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5951</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mortakee</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5957</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a fisherman / diver</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Sea Disaster</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Boat</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>4315 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>anonymous</td>
      <td>Nulos</td>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>Mrs. Despo Snow-Christensen</td>
      <td>F</td>
      <td>Shark brushed past, minor injuries if any</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3718</th>
      <td>1960</td>
      <td>Unprovoked</td>
      <td>Lester McDougall</td>
      <td>M</td>
      <td>Left thigh lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3720</th>
      <td>1960</td>
      <td>Unprovoked</td>
      <td>Harry Bicknell</td>
      <td>M</td>
      <td>Right shoulder lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3722</th>
      <td>1960</td>
      <td>Provoked</td>
      <td>Ken O\92Connell</td>
      <td>M</td>
      <td>Shark knocked him off surf-ski, he inhaled wat...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3723</th>
      <td>1960</td>
      <td>Unprovoked</td>
      <td>Don Morrissey</td>
      <td>M</td>
      <td>Scratches on right upper arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3725</th>
      <td>1960</td>
      <td>Provoked</td>
      <td>Fisheries trainee</td>
      <td>M</td>
      <td>Left wrist bitten by netted shark placed in bo...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3729</th>
      <td>1960</td>
      <td>Invalid</td>
      <td>B. Hooper</td>
      <td>M</td>
      <td>Swept off rocks &amp; presumed to have drowned, sh...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3730</th>
      <td>1960</td>
      <td>Unprovoked</td>
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
      <th>Type</th>
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
      <td>Provoked</td>
      <td>male</td>
      <td>Nulos</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
  </tbody>
</table>
</div>



```python
#Arreglo datos en 'Type'
df6.loc[df6['Type']=='Boating', 'Type'] = 'Provoked'
df6.loc[df6['Type']=='Boat', 'Type'] = 'Provoked'
df6.loc[df6['Type']=='Sea Disaster', 'Type'] = 'Provoked'

display(df6.loc[df6['Type']=='Unprovoked',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Type']=='Provoked',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Type']=='Invalid',['Year','Type','Name','Activity','Injury','Fatal (Y/N)']])

print(set(df6['Type']))
print('Type',len(set(df6['Type'])))
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>Surfing</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>Surfing</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Wading</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Swimming</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>Kite surfing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>Boogie boarding</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>Surfing</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>Body boarding</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>Spearfishing</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>Surfing</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>Surfing</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>Wading</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>Snorkeling</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>SUP Foil boarding</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>Surfing</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>Swimming</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>Surfing</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>Surfing</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>Spearfishing</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Surfing</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>NaN</td>
      <td>Minor injury to toes</td>
      <td>N</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Puncture wounds to foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Michael Dornellas</td>
      <td>Scuba Diving</td>
      <td>Face bruised when partly blind shark collided ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>Wading</td>
      <td>5 tiny puncture marks to lower leg, treated wi...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5957</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a fisherman / diver</td>
      <td>Diving</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>Diving</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Bathing</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>Sponge diving</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>Standing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>Wading</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>Pearl diving</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>Swimming in pool formed by construction of a w...</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>Fishing</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>Swimming around anchored ship</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Crew swimming alongside their anchored ship</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>4 men were bathing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>Wreck of  large double sailing canoe</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>Swimming</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>Fishing</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>Wading</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>Swimming</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>NaN</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>Fishing</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>Fishing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>Fishing</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Diving</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>Pearl diving</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>Swimming</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>Swimming</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4386 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Stratton</td>
      <td>Fishing</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Ian Watkins</td>
      <td>Kayaking</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>Lobstering</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>Fishing</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Raines</td>
      <td>Fishing in Alabama Deep Fishing Rodeo</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Mark Davis</td>
      <td>Fishing for squid</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Roger Brissom</td>
      <td>Fishing</td>
      <td>Fin of hooked shark injured fisherman's forear...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>37</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>24' boat Shark Tagger Occupant Keith Poe</td>
      <td>Fishing for sharks</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>39</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Nathan Oliver</td>
      <td>Fishing</td>
      <td>Right thigh injured by hooked pregnant female ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>47</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Brad Vale</td>
      <td>Spearfishing</td>
      <td>No injury but shark punctured his wetsuit afte...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>female</td>
      <td>Teasing a shark</td>
      <td>Arm grabbed PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>65</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Fishing</td>
      <td>Foot bitten by landed shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>70</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Teva Tokoragi</td>
      <td>Spearfishing</td>
      <td>Severe lacerations to right forearm, hand and ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>80</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Henry Kreckman</td>
      <td>NaN</td>
      <td>Minor injury to chest PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>94</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Dev De Lange</td>
      <td>Kayak fishing</td>
      <td>No injury, shark capsized kayak</td>
      <td>N</td>
    </tr>
    <tr>
      <th>98</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupants: Hamza Humaid Al Sahra\92a &amp; 5 crew</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark leapt into boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Occupant: Grant Wardell</td>
      <td>Kayak Fishing</td>
      <td>No injury, kayak damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>6 m boat: occupants  Stephen &amp; Andrew Crust</td>
      <td>Fishing</td>
      <td>No injury, shark rammed boat &amp; bit motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>128</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Jordan Pavacich</td>
      <td>Kayak Fishing</td>
      <td>No injury, shark rammed kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>147</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Dylan Marks</td>
      <td>Kayak Fishing</td>
      <td>Laceration to dorsum of foot by hooked shark  ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>160</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Richard Shafer</td>
      <td>Spearfishing</td>
      <td>Right hand bitten  PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>165</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Austin Lorber</td>
      <td>Kayak Fishing</td>
      <td>No injury to occupant. Kayak bitten by gaffed ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>184</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Stephen</td>
      <td>Swimming</td>
      <td>Minor lacerations to forearm when he grabbed s...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>218</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Kayak: Occupant Kelly Janse van Rensburg</td>
      <td>Kayak Fishing</td>
      <td>No injury but kayak bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>222</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Dinghy: Occupant Robbie Graham</td>
      <td>Fishing</td>
      <td>Bruised in falling overboard as shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>223</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>David Villegas Mora</td>
      <td>Fishing</td>
      <td>Right hand bitten by hooked shark PROVOKED INC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>225</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Avalon, a carbon kevlar monohull: 8 occupants</td>
      <td>Transatlantic Rowing</td>
      <td>No injury, shark bit rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>230</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Racing scull: Occupant Trevor Carter</td>
      <td>Rowing</td>
      <td>No injury, shark's teeth scratched hull</td>
      <td>N</td>
    </tr>
    <tr>
      <th>231</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Michael Pollard</td>
      <td>Shark fishing</td>
      <td>Lacerations to calf by hooked shark PROVOKED I...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>233</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>22-ft boat.  Occupant Captain Scott Fitzgerald</td>
      <td>Fishing</td>
      <td>No injury but shark bit trolling motor &amp; ramme...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5679</th>
      <td>1865</td>
      <td>Provoked</td>
      <td>R.H. Barrett, pilot holding steering oar of wh...</td>
      <td>Boarding a ship</td>
      <td>No injury to pilot, oar bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5680</th>
      <td>1864</td>
      <td>Provoked</td>
      <td>fisherman</td>
      <td>Dragging a shark</td>
      <td>Knee bitten PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5716</th>
      <td>1860</td>
      <td>Provoked</td>
      <td>a Cook's Islander</td>
      <td>43-ton schooner Irene capsized &amp; sank</td>
      <td>Probable drowning</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5728</th>
      <td>1855</td>
      <td>Provoked</td>
      <td>sailor</td>
      <td>ship William Penn grounded &amp; broke apart</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5743</th>
      <td>1852</td>
      <td>Provoked</td>
      <td>William Stannard</td>
      <td>Fishing</td>
      <td>Foot bitten by hooked shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5749</th>
      <td>1852</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Wreck of the steamship Birkenhead</td>
      <td>FATAL. All of the women &amp; children on board su...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5766</th>
      <td>1847</td>
      <td>Provoked</td>
      <td>Spicer</td>
      <td>Wreck of the Sovereign</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5770</th>
      <td>1846</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Wreck of the USS Somers</td>
      <td>FATAL, some were taken by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5779</th>
      <td>1842</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Harassing a shark</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
    <tr>
      <th>5785</th>
      <td>1840</td>
      <td>Provoked</td>
      <td>A dinghy</td>
      <td>Sailing</td>
      <td>No injury to occupant, shark seized stern post</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5806</th>
      <td>1829</td>
      <td>Provoked</td>
      <td>Ned &amp; Pawn</td>
      <td>Wreck of the schooner Driver</td>
      <td>FATAL x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5815</th>
      <td>1826</td>
      <td>Provoked</td>
      <td>Lieutenant Edward Smith</td>
      <td>HBM Magpie foundered in a squall</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5830</th>
      <td>1804</td>
      <td>Provoked</td>
      <td>boat</td>
      <td>NaN</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5834</th>
      <td>1788</td>
      <td>Provoked</td>
      <td>boat</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bit oar and rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5839</th>
      <td>1776</td>
      <td>Provoked</td>
      <td>Occupants of skin boats</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5870</th>
      <td>0</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>Shipwrecked Persian Fleet</td>
      <td>Herodotus tells of sharks attacking men in the...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5871</th>
      <td>0</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Vase depicts shipwrecked sailors, one of whom ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5885</th>
      <td>0</td>
      <td>Provoked</td>
      <td>male</td>
      <td>NaN</td>
      <td>Cut to arm while roping shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5889</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Phillip Peters</td>
      <td>NaN</td>
      <td>Bitten by captive sharks PROVOKED INCIDENTS</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5902</th>
      <td>0</td>
      <td>Provoked</td>
      <td>4.8-metre skiboat, Occupants: Rod Salm &amp; 4 fri...</td>
      <td>Fishing</td>
      <td>No injury to occupants, shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5914</th>
      <td>0</td>
      <td>Provoked</td>
      <td>a chief</td>
      <td>Attempting to drive shark from area</td>
      <td>Speared shark broke outrigger of canoe throwin...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5916</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Carl Bruster</td>
      <td>Skin diving. Grabbed shark's tail; shark turne...</td>
      <td>Ankle punctured &amp; lacerated, hands abraded PRO...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5940</th>
      <td>0</td>
      <td>Provoked</td>
      <td>John Fenton</td>
      <td>Testing movie camera in full diving dress</td>
      <td>Shark bit diver's sleeve after he patted it on...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5944</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Sandrillio</td>
      <td>Shark fishing, knocked overboard</td>
      <td>FATAL, hip bitten  PROVOKED INCIDENT</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Provoked</td>
      <td>C.</td>
      <td>A group of survivors on a raft for 17-days</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Provoked</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>NaN</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>Carrying a supposedly dead shark by its mouth</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Provoked</td>
      <td>pilot</td>
      <td>Spent 8 days in dinghy</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Provoked</td>
      <td>male</td>
      <td>Aircraft ditched in the sea, swimming ashore</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>Wooden fishing boat</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>1087 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Activity</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>50</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Jack O'Neill</td>
      <td>Surfing</td>
      <td>No injury, board damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>73</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>a British citizen</td>
      <td>NaN</td>
      <td>"Serious"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>75</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Maximo Trinidad</td>
      <td>SUP</td>
      <td>Fell off board when spinner shark leapt from t...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>81</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>unknown</td>
      <td>Surfing</td>
      <td>Board reportedly bumped by shark. No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>90</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>Richard Branson</td>
      <td>Feeding stingrays?</td>
      <td>Minor injury to wrist from Southern stingray</td>
      <td>N</td>
    </tr>
    <tr>
      <th>91</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Surfing</td>
      <td>No injury, knocked off board</td>
      <td>N</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Ryla Underwood</td>
      <td>Surfing</td>
      <td>Lower left leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>126</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Surfing</td>
      <td>Left foot bitten by eel</td>
      <td>N</td>
    </tr>
    <tr>
      <th>154</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>young boy</td>
      <td>NaN</td>
      <td>Wound to right lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>159</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Minor injury when he attempted to touch a fish.</td>
      <td>N</td>
    </tr>
    <tr>
      <th>163</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>female</td>
      <td>Floating</td>
      <td>2' cut to dorsum of foot, 2 puncture wounds to...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>170</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugene Finney</td>
      <td>Treading water</td>
      <td>Laceration to back</td>
      <td>N</td>
    </tr>
    <tr>
      <th>171</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Joe Termini</td>
      <td>Swimming</td>
      <td>Parallel lacerations to torso inconsistent wit...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>181</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>female</td>
      <td>Swimming</td>
      <td>Minor lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>187</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Lily Kumpe</td>
      <td>Surfing</td>
      <td>Bruises and abrasions to face, chin, chest, bo...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>215</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Diego Gomes Mota</td>
      <td>Surfing</td>
      <td>Injury to left thigh from unidentified species...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugenio Masala</td>
      <td>Diving</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>234</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Diane Ellis</td>
      <td>Surfing &amp; filming dolphins</td>
      <td>Board snapped in two</td>
      <td>N</td>
    </tr>
    <tr>
      <th>237</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Rob Konrad</td>
      <td>Swimming after falling overboard</td>
      <td>During his 16-hour swim to shore, he was circl...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>244</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>5 people claimed to have been injured by a "ba...</td>
      <td>Swimming</td>
      <td>Minor cuts on feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>277</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Beau Browning</td>
      <td>Surfing</td>
      <td>A hoax, no shark involvement</td>
      <td>N</td>
    </tr>
    <tr>
      <th>285</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>child</td>
      <td>NaN</td>
      <td>Shark involvement not confirmed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>303</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Cuban refugees</td>
      <td>Sea disaster</td>
      <td>Shark involvement prior to death not confirmed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>John Petty</td>
      <td>Shark diving</td>
      <td>Missing after a dive, shark involvement consid...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>337</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Jimmy Roseman</td>
      <td>Diving</td>
      <td>No injury. No attack. 12' white shark appeared...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>348</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Michael McGregor</td>
      <td>Diving for lobsters</td>
      <td>Shark bites may have been post mortem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>354</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Jason Dimitri</td>
      <td>Scuba diving / culling lionfish</td>
      <td>Caribbean reef shark buzzed him. No injury, no...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>355</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Myxie Ryan</td>
      <td>NaN</td>
      <td>Injuries to wrist/hand by a mackerel, not a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>410</th>
      <td>2013</td>
      <td>Invalid</td>
      <td>Charlotte Brynn</td>
      <td>Marathon swimming</td>
      <td>Puncture wound to torso. Reported as a bite by...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>434</th>
      <td>2013</td>
      <td>Invalid</td>
      <td>Thierry Frennet</td>
      <td>Swimming</td>
      <td>Scrape to right forearm. Frennet says inflicte...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5645</th>
      <td>1872</td>
      <td>Invalid</td>
      <td>Mr. Manning</td>
      <td>boat capsized</td>
      <td>Probable drowning</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5647</th>
      <td>1871</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Human remains recovered from 11' shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5662</th>
      <td>1870</td>
      <td>Invalid</td>
      <td>Sub Lieut. Bowyer of H.M.S. Chile</td>
      <td>Canoeing</td>
      <td>Shark bit canoe in half &amp; bit man. Note: There...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5664</th>
      <td>1869</td>
      <td>Invalid</td>
      <td>Christian Frederick</td>
      <td>Fell overboard</td>
      <td>FATAL, but shark involvement prior to death wa...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5675</th>
      <td>1866</td>
      <td>Invalid</td>
      <td>Mr. Groves</td>
      <td>Fell overboard</td>
      <td>Thought to have been taken by a shark. Body wa...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5687</th>
      <td>1864</td>
      <td>Invalid</td>
      <td>Mr. Warren, Jr.</td>
      <td>Swimming</td>
      <td>Presumed Fatal, but shark involvement not conf...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5692</th>
      <td>1863</td>
      <td>Invalid</td>
      <td>Mr. J. Canham</td>
      <td>Swimming, caught in strong backwash &amp; disappeared</td>
      <td>Shark caught 9 days later contained human rema...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5699</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Possible drowning and scavenging</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5719</th>
      <td>1858</td>
      <td>Invalid</td>
      <td>male</td>
      <td>Swimming</td>
      <td>Thought to have been taken by a shark/s. Body ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5720</th>
      <td>1858</td>
      <td>Invalid</td>
      <td>3 males</td>
      <td>Swimming</td>
      <td>Thought to have been taken by a shark/s. Bodie...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5733</th>
      <td>1855</td>
      <td>Invalid</td>
      <td>C.T. Clark</td>
      <td>Swimming</td>
      <td>No injury &amp; although reported as an attack, it...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5740</th>
      <td>1853</td>
      <td>Invalid</td>
      <td>a young man</td>
      <td>He was fighting a shark when his boat capsized...</td>
      <td>His gold watch was later found in a shark but...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5742</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Edward Graham</td>
      <td>Swimming</td>
      <td>Shark involvement prior to death was not confi...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>NaN</td>
      <td>Death preceded shark involvement</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5761</th>
      <td>1849</td>
      <td>Invalid</td>
      <td>William Henry Elliott</td>
      <td>boat capsized</td>
      <td>Torso bitten but may have been postmorem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5768</th>
      <td>1847</td>
      <td>Invalid</td>
      <td>a young sailor</td>
      <td>Swimming</td>
      <td>Disappeared, thought to have been taken by a s...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5787</th>
      <td>1839</td>
      <td>Invalid</td>
      <td>Mr.Johnson (male)</td>
      <td>NaN</td>
      <td>"Drowned, 2 days later his head was bitten off...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5793</th>
      <td>1837</td>
      <td>Invalid</td>
      <td>adult male, a sailor</td>
      <td>NaN</td>
      <td>Shark caught contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Shark caught, contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5801</th>
      <td>1831</td>
      <td>Invalid</td>
      <td>Robert Dudlow</td>
      <td>Boat capsized, clinging to line</td>
      <td>Drowned, no shark involvement</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5817</th>
      <td>1825</td>
      <td>Invalid</td>
      <td>Nelson</td>
      <td>NaN</td>
      <td>Arms severed, but he survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5819</th>
      <td>1819</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>No injury / No attack</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5820</th>
      <td>1818</td>
      <td>Invalid</td>
      <td>male</td>
      <td>NaN</td>
      <td>Probable drowning</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5829</th>
      <td>1805</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>human remains (male) found in shark\92s gut</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5841</th>
      <td>1767</td>
      <td>Invalid</td>
      <td>Samuel Matthews</td>
      <td>Bathing</td>
      <td>Lacerations to arm &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5855</th>
      <td>1642</td>
      <td>Invalid</td>
      <td>crew member of the Nieuwstadt</td>
      <td>Went overboard</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5917</th>
      <td>0</td>
      <td>Invalid</td>
      <td>Dan Hogan</td>
      <td>Scuba diving</td>
      <td>Said to be fatal but incident highly questionable</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5922</th>
      <td>0</td>
      <td>Invalid</td>
      <td>Val Valentine</td>
      <td>Diving</td>
      <td>A 4.3 m [14'] shark made threat display. No in...</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>519 rows × 6 columns</p>
</div>


    {'Provoked', 'Invalid', 'Unprovoked'}
    Type 3



```python
#Arreglo datos en 'Sex '
df6.loc[df6['Sex ']=='.', 'Sex '] = 'N.A.'
df6.loc[df6['Sex ']=='N', 'Sex '] = 'N.A.'
df6.loc[df6['Sex ']=='Nulos', 'Sex '] = 'N.A.'

df6.loc[df6['Sex ']=='lli', 'Sex '] = 'M'
df6.loc[df6['Sex ']=='M ', 'Sex '] = 'M'

display(df6.loc[df6['Sex ']=='M',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='F',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Sex ']=='N.A.',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])

print(set(df6['Sex ']))
print('Sex ',len(set(df6['Sex '])))
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>32</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Puncture wounds to foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>33</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Michael Dornellas</td>
      <td>M</td>
      <td>Face bruised when partly blind shark collided ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>35</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Mark Davis</td>
      <td>M</td>
      <td>No injury. Hull bitten, tooth fragment recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>36</th>
      <td>2016</td>
      <td>Provoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Provoked</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Provoked</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Provoked</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4838 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Minor injury to toes</td>
      <td>N</td>
    </tr>
    <tr>
      <th>34</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>5 tiny puncture marks to lower leg, treated wi...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Buttocks, thigh, left hand &amp; wrist injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>48</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Marin Alice Melton</td>
      <td>F</td>
      <td>Injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>57</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Maria Korcsmaros \n</td>
      <td>F</td>
      <td>Injuries to arm and shoulder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>59</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Mary Marcus</td>
      <td>F</td>
      <td>Puncture wounds to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>60</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Krystal Magee</td>
      <td>F</td>
      <td>Lacerations and puncture wounds to foot and ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>61</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Back, arm &amp; hand injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>63</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>female</td>
      <td>F</td>
      <td>Arm grabbed PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>76</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>J. Orr</td>
      <td>F</td>
      <td>Minor injury to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>89</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Patricia Howe</td>
      <td>F</td>
      <td>Avulsion injury to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>92</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Foot nipped</td>
      <td>N</td>
    </tr>
    <tr>
      <th>96</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Kaya Waldman</td>
      <td>F</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Cristina Ojeda-Thies</td>
      <td>F</td>
      <td>Lacerations to left forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>111</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Tamsin Scott</td>
      <td>F</td>
      <td>Lacerations to both hands and forearms</td>
      <td>N</td>
    </tr>
    <tr>
      <th>113</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>116</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Ryla Underwood</td>
      <td>F</td>
      <td>Lower left leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>118</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Jill Kruse</td>
      <td>F</td>
      <td>Injury to right ankle/calf &amp; hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>129</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Meti Kershner</td>
      <td>F</td>
      <td>Laceration to forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>137</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Laceration to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>146</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Caterina Gennaro</td>
      <td>F</td>
      <td>No injury, shark struck board, tossing her int...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>150</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Jane Neame</td>
      <td>F</td>
      <td>Left foot &amp; ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>152</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Elinor Dempsey</td>
      <td>F</td>
      <td>No injury, surfboard bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>157</th>
      <td>2015</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5435</th>
      <td>1892</td>
      <td>Unprovoked</td>
      <td>Mrs. Coe</td>
      <td>F</td>
      <td>Abrasions to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5508</th>
      <td>1886</td>
      <td>Invalid</td>
      <td>2 women</td>
      <td>F</td>
      <td>The body of one woman had been bitten by a sha...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5529</th>
      <td>1884</td>
      <td>Provoked</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL            Leg severed by harpooned shar...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5533</th>
      <td>1884</td>
      <td>Unprovoked</td>
      <td>Miss Warren</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5569</th>
      <td>1880</td>
      <td>Unprovoked</td>
      <td>a widow</td>
      <td>F</td>
      <td>Hands, forearm &amp; left thigh lacerated, radial ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5574</th>
      <td>1880</td>
      <td>Unprovoked</td>
      <td>Teresa Bonnell</td>
      <td>F</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5595</th>
      <td>1878</td>
      <td>Unprovoked</td>
      <td>Dolores Margarita Corrales y Roa</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5610</th>
      <td>1877</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Ankle injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5698</th>
      <td>1862</td>
      <td>Unprovoked</td>
      <td>The widowed Marchioness of Lendinez</td>
      <td>F</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5705</th>
      <td>1862</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5730</th>
      <td>1855</td>
      <td>Unprovoked</td>
      <td>child</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>F</td>
      <td>Death preceded shark involvement</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5760</th>
      <td>1849</td>
      <td>Unprovoked</td>
      <td>Mrs. Cracton</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5798</th>
      <td>1834</td>
      <td>Unprovoked</td>
      <td>Kaugatava Orurutm</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5799</th>
      <td>1832</td>
      <td>Unprovoked</td>
      <td>Aboriginal female</td>
      <td>F</td>
      <td>Leg severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5832</th>
      <td>1800</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>F</td>
      <td>FATAL, all onboard were killed by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5833</th>
      <td>1791</td>
      <td>Unprovoked</td>
      <td>female, an Australian aboriginal</td>
      <td>F</td>
      <td>FATAL, "bitten in two"</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5879</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Lassie</td>
      <td>F</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5883</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Martha Hatagouei</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5888</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Leg severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5890</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Danniell Washington</td>
      <td>F</td>
      <td>Severe abrasion to forearm from captive shark ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5896</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Sametra Mestri</td>
      <td>F</td>
      <td>Hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5910</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female, a Hae Nyeo</td>
      <td>F</td>
      <td>FATAL, injured while diving, then shark bit her</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5913</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5918</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jill Reed</td>
      <td>F</td>
      <td>Shoulder scratched, swim fin bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5921</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>woman</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>585 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Stratton</td>
      <td>N.A.</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Raines</td>
      <td>N.A.</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>81</th>
      <td>2016</td>
      <td>Invalid</td>
      <td>unknown</td>
      <td>N.A.</td>
      <td>Board reportedly bumped by shark. No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>109</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>6 m boat: occupants  Stephen &amp; Andrew Crust</td>
      <td>N.A.</td>
      <td>No injury, shark rammed boat &amp; bit motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>225</th>
      <td>2015</td>
      <td>Provoked</td>
      <td>Avalon, a carbon kevlar monohull: 8 occupants</td>
      <td>N.A.</td>
      <td>No injury, shark bit rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>241</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Jeff Brown</td>
      <td>N.A.</td>
      <td>Lacerations to both feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>243</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Passenger ferry Norman Atlantic</td>
      <td>N.A.</td>
      <td>Of 9 bodies recovered, one was bitten by a shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>244</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>5 people claimed to have been injured by a "ba...</td>
      <td>N.A.</td>
      <td>Minor cuts on feet</td>
      <td>N</td>
    </tr>
    <tr>
      <th>254</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Boat: occupants: Matt Mitchell &amp; 2 other people</td>
      <td>N.A.</td>
      <td>Shark bumped boat, no injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>285</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>child</td>
      <td>N.A.</td>
      <td>Shark involvement not confirmed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>291</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Miller Diggs</td>
      <td>N.A.</td>
      <td>Laceration to left foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>307</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>child</td>
      <td>N.A.</td>
      <td>Minor injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>343</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Inflatable boat</td>
      <td>N.A.</td>
      <td>No injury to occupants, shark bit pontoon</td>
      <td>N</td>
    </tr>
    <tr>
      <th>366</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Dinghy. Occupants: Jeff Kurr and Andy Casagrande</td>
      <td>N.A.</td>
      <td>No injury to occupants, shark nudged and bit boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>478</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Lacerations to right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>517</th>
      <td>2012</td>
      <td>Unprovoked</td>
      <td>teen</td>
      <td>N.A.</td>
      <td>Minor injury to elbow</td>
      <td>N</td>
    </tr>
    <tr>
      <th>524</th>
      <td>2012</td>
      <td>Provoked</td>
      <td>M. Malabon</td>
      <td>N.A.</td>
      <td>Minor laceration to hand  PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>530</th>
      <td>2012</td>
      <td>Provoked</td>
      <td>dinghy</td>
      <td>N.A.</td>
      <td>No injury, shark grabbed outboard motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>548</th>
      <td>2012</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Leg struck. Initally reported as a shark attac...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>582</th>
      <td>2012</td>
      <td>Provoked</td>
      <td>crayfish boat. Occupants: Dave &amp; Mitchell Dupe...</td>
      <td>N.A.</td>
      <td>No injury to occupants. Shark bit propelle, ro...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>595</th>
      <td>2012</td>
      <td>Provoked</td>
      <td>8m inflatable boat. Occupants: Bhad Battle &amp; K...</td>
      <td>N.A.</td>
      <td>No injury to occupants, boat damaged</td>
      <td>N</td>
    </tr>
    <tr>
      <th>598</th>
      <td>2012</td>
      <td>Unprovoked</td>
      <td>J. Graden</td>
      <td>N.A.</td>
      <td>No injury, shark bit swim fin</td>
      <td>N</td>
    </tr>
    <tr>
      <th>616</th>
      <td>2011</td>
      <td>Invalid</td>
      <td>Dave Fordson</td>
      <td>N.A.</td>
      <td>Killed by a shark or crocodile.</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>626</th>
      <td>2011</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Arm bitten by captive shark PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>647</th>
      <td>2011</td>
      <td>Unprovoked</td>
      <td>M. Filipe</td>
      <td>N.A.</td>
      <td>No injury, shark bit surfboard</td>
      <td>N</td>
    </tr>
    <tr>
      <th>688</th>
      <td>2011</td>
      <td>Provoked</td>
      <td>16' Dreamcatcher. Occupant: Ian Bussus</td>
      <td>N.A.</td>
      <td>No injury, shark slammed into boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>733</th>
      <td>2011</td>
      <td>Provoked</td>
      <td>A 'tinnie". Occupants :Paul Sweeny, Paul Nieuw...</td>
      <td>N.A.</td>
      <td>No injury, shark nudged boat and bit propeller</td>
      <td>N</td>
    </tr>
    <tr>
      <th>844</th>
      <td>2009</td>
      <td>Provoked</td>
      <td>Surf boat with 5 lifesavers on board</td>
      <td>N.A.</td>
      <td>No injury to occupants; shark bit steering oar</td>
      <td>N</td>
    </tr>
    <tr>
      <th>941</th>
      <td>2009</td>
      <td>Provoked</td>
      <td>7.2 m boat. Occupant Kelvin Travers</td>
      <td>N.A.</td>
      <td>No injury to occupant, shark removed small aux...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>947</th>
      <td>2009</td>
      <td>Unprovoked</td>
      <td>4 poachers</td>
      <td>N.A.</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5628</th>
      <td>1874</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Shark and boat collided. No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5635</th>
      <td>1874</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>2 people out of +70 survived, one of whom was ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5644</th>
      <td>1872</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>FATAL, some were taken by sharks</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5668</th>
      <td>1868</td>
      <td>Provoked</td>
      <td>boat, occupants: John Griffiths &amp; Thomas Johnson</td>
      <td>N.A.</td>
      <td>No injury to occupants, shark's teeth embedded...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5679</th>
      <td>1865</td>
      <td>Provoked</td>
      <td>R.H. Barrett, pilot holding steering oar of wh...</td>
      <td>N.A.</td>
      <td>No injury to pilot, oar bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5767</th>
      <td>1847</td>
      <td>Unprovoked</td>
      <td>a native</td>
      <td>N.A.</td>
      <td>Foot severed at ankle joint</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5779</th>
      <td>1842</td>
      <td>Provoked</td>
      <td>male</td>
      <td>N.A.</td>
      <td>Lacerations to leg  PROVOKED INCIDENT</td>
      <td>n</td>
    </tr>
    <tr>
      <th>5785</th>
      <td>1840</td>
      <td>Provoked</td>
      <td>A dinghy</td>
      <td>N.A.</td>
      <td>No injury to occupant, shark seized stern post</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Shark caught, contained human remains</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5795</th>
      <td>1836</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>No details, it was the year the first settlers...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5818</th>
      <td>1822</td>
      <td>Unprovoked</td>
      <td>slaves</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5825</th>
      <td>1816</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5830</th>
      <td>1804</td>
      <td>Provoked</td>
      <td>boat</td>
      <td>N.A.</td>
      <td>No injury to occupants</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5834</th>
      <td>1788</td>
      <td>Provoked</td>
      <td>boat</td>
      <td>N.A.</td>
      <td>No injury to occupants, shark bit oar and rudder</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5839</th>
      <td>1776</td>
      <td>Provoked</td>
      <td>Occupants of skin boats</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>Nulos</td>
    </tr>
    <tr>
      <th>5857</th>
      <td>1637</td>
      <td>Unprovoked</td>
      <td>Hindu pilgrims</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5858</th>
      <td>1617</td>
      <td>Unprovoked</td>
      <td>Indian people</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5865</th>
      <td>500</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>N.A.</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5871</th>
      <td>0</td>
      <td>Provoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Vase depicts shipwrecked sailors, one of whom ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5875</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5887</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Injury required 16 stitches</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5892</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Passenger &amp; crew</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5902</th>
      <td>0</td>
      <td>Provoked</td>
      <td>4.8-metre skiboat, Occupants: Rod Salm &amp; 4 fri...</td>
      <td>N.A.</td>
      <td>No injury to occupants, shark bumped boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5909</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Albert Raiti</td>
      <td>N.A.</td>
      <td>Lacerations to hands and knee</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5927</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Recovered</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Provoked</td>
      <td>C.</td>
      <td>N.A.</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>N.A.</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>569 rows × 6 columns</p>
</div>


    {'F', 'M', 'N.A.'}
    Sex  3



```python
#Arreglo datos en 'Fatal (Y/N)'
df6.loc[df6['Fatal (Y/N)']=='#VALUE!', 'Fatal (Y/N)'] = 'UNDETERMINED'
df6.loc[df6['Fatal (Y/N)']=='F', 'Fatal (Y/N)'] = 'UNDETERMINED'
df6.loc[df6['Fatal (Y/N)']=='Nulos', 'Fatal (Y/N)'] = 'UNDETERMINED'

df6.loc[df6['Fatal (Y/N)']=='N ', 'Fatal (Y/N)'] = 'N'
df6.loc[df6['Fatal (Y/N)']==' N', 'Fatal (Y/N)'] = 'N'
df6.loc[df6['Fatal (Y/N)']=='n', 'Fatal (Y/N)'] = 'N'

display(df6.loc[df6['Fatal (Y/N)']=='Y',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='N',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='UNDETERMINED',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])
display(df6.loc[df6['Fatal (Y/N)']=='UNKNOWN',['Year','Type','Name','Sex ','Injury','Fatal (Y/N)']])

print(set(df6['Fatal (Y/N)']))
print('Fatal (Y/N)',len(set(df6['Fatal (Y/N)'])))
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>David Jewell</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>52</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Doreen Collyer</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>56</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Ben Gerring</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>72</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nicole Malignon</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>83</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Maika Tabua</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>108</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Adrian Esteban Rafael</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>125</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Albertina Cavel</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>164</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Damien Johnson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Yves Berthelot</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>208</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Margaret Cruse</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>214</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Elio Canestri</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>217</th>
      <td>2015</td>
      <td>Invalid</td>
      <td>Eugenio Masala</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>219</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>226</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Talon Bishop</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>227</th>
      <td>2015</td>
      <td>Unprovoked</td>
      <td>Tadashi Nakahara</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>242</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Jay Muscat</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>248</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Daniel Smith</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>251</th>
      <td>2014</td>
      <td>Provoked</td>
      <td>Rameshwar Ram Dhauro</td>
      <td>M</td>
      <td>FATAL, arm bitten by shark hauled on deck     ...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>278</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Paul Wilcox</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>303</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Cuban refugees</td>
      <td>M</td>
      <td>Shark involvement prior to death not confirmed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>310</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>John Petty</td>
      <td>M</td>
      <td>Missing after a dive, shark involvement consid...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>347</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Christine Armstrong</td>
      <td>F</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>348</th>
      <td>2014</td>
      <td>Invalid</td>
      <td>Michael McGregor</td>
      <td>M</td>
      <td>Shark bites may have been post mortem</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>349</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Friedrich Burgstaller.</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>360</th>
      <td>2014</td>
      <td>Unprovoked</td>
      <td>Sam Kellett</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>373</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Patrick Briney</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>374</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Zac Young</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>376</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Chris Boyd</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>390</th>
      <td>2013</td>
      <td>Unprovoked</td>
      <td>Burgert Van Der Westhuizen</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>416</th>
      <td>2013</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5942</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5943</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>an Indian</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5944</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Sandrillio</td>
      <td>M</td>
      <td>FATAL, hip bitten  PROVOKED INCIDENT</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5948</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Gilbertese fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5949</th>
      <td>0</td>
      <td>Provoked</td>
      <td>C.</td>
      <td>N.A.</td>
      <td>FATAL, shark leapt into raft and bit the man w...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5952</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>an old fisherman</td>
      <td>M</td>
      <td>FATAL, foot lacerated &amp; crushed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5953</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a local dignitary</td>
      <td>M</td>
      <td>FATAL, femoral artery severed, died 12 days la...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5954</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>I.A.S. C. driver</td>
      <td>M</td>
      <td>FATAL, fell into water when shark seized his r...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5955</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL, left leg bitten with severe blood loss</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5956</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>FATAL, died of sepsis</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5959</th>
      <td>0</td>
      <td>Provoked</td>
      <td>8 US airmen in the water, 1 was bitten by a shark</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Fatal x 2</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a servant</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Indian boy</td>
      <td>M</td>
      <td>FATAL, leg severed</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>3 Japanese divers</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>20 Fijians</td>
      <td>N.A.</td>
      <td>FATAL, 18 people  were killed by sharks, 2 sur...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a native fisherman</td>
      <td>M</td>
      <td>FATAL, body not recovered but shark was caught...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a young Scotsman</td>
      <td>M</td>
      <td>FATAL, leg stripped of flesh</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>boy</td>
      <td>M</td>
      <td>FATAL, knocked overboard by tail of shark &amp; ca...</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>fisherman</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Arab boy</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ahmun</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Coast Guard personnel</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jules Patterson</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>FATAL. "Shark bit him in half, carrying away t...</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>1552 rows × 6 columns</p>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Chucky Luciano</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rory Angiolella</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Stratton</td>
      <td>N.A.</td>
      <td>Shark rammed boat. No injury to occupant</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Rylie Williams</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Fraser Penman</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Austin Moore</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Tyler McQuillen</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Sam Cumiskey</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Laurent Chardard</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>David Cassetty</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Johnny Stoch</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Connor Baxter</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Nolan Tyler</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Justus Franz</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Ian Watkins</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Warren Sapp</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Curran See &amp; Harry Lake</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Zebulon Critchlow</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Steve Cutbirth</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Scott van Burck</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Occupant: Ben Raines</td>
      <td>N.A.</td>
      <td>No injury, shark bit trolling motor</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>5928</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Dalton Baldwin</td>
      <td>M</td>
      <td>No injury, bumped by shark which took speared ...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5929</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Les Bishop</td>
      <td>M</td>
      <td>Bumped by sharks</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5931</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Right hand severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5932</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Arm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5933</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Right leg lacerated &amp; surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5934</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, a sponge Diver</td>
      <td>M</td>
      <td>Lower leg and forearm severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5935</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>girl</td>
      <td>F</td>
      <td>Leg injured</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5936</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Ross Doe</td>
      <td>M</td>
      <td>Shoulder abraded by skin of shark</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5937</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Fijian girl</td>
      <td>F</td>
      <td>"Severely injured when fish were seized by shark"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5939</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Horton Chase</td>
      <td>M</td>
      <td>Abrasions &amp; bruises hip to ankle</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5940</th>
      <td>0</td>
      <td>Provoked</td>
      <td>John Fenton</td>
      <td>M</td>
      <td>Shark bit diver's sleeve after he patted it on...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5945</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5946</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Dusty Rhodes</td>
      <td>M</td>
      <td>No injury</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5947</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Survived</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5950</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>American male</td>
      <td>M</td>
      <td>Buttock bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5951</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mortakee</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5957</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a fisherman / diver</td>
      <td>M</td>
      <td>Buttocks bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5958</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>Foot lacerated, surgically amputated</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5960</th>
      <td>0</td>
      <td>Provoked</td>
      <td>boy</td>
      <td>M</td>
      <td>4 finger severed by 'dead' shark. PROVOKED ACC...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5961</th>
      <td>0</td>
      <td>Provoked</td>
      <td>pilot</td>
      <td>M</td>
      <td>No injury, but shark removed the heel &amp; part o...</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Provoked</td>
      <td>male</td>
      <td>M</td>
      <td>Shark bumped him</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Provoked</td>
      <td>Occupant:     Mr. Maciotta</td>
      <td>M</td>
      <td>No injury to occupant; shark capsized boat</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Psarofa-gomenes</td>
      <td>M</td>
      <td>Head bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Madelaine Dalton</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Jaringoorli</td>
      <td>M</td>
      <td>Lacerations to thigh</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>James Kelley</td>
      <td>M</td>
      <td>2-inch lacerations</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>crewman</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>"youthful male"</td>
      <td>M</td>
      <td>"Lost leg"</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>Mr. Masury</td>
      <td>M</td>
      <td>Foot severed</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>A chiefess</td>
      <td>F</td>
      <td>Ankle bitten</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>4325 rows × 6 columns</p>
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
      <th>Type</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Waade Madigan and Dr Seyong Kim</td>
      <td>M</td>
      <td>No injury, but sharks repeatedly hit their fin...</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>1844</th>
      <td>2000</td>
      <td>Invalid</td>
      <td>Ricky Stringer</td>
      <td>M</td>
      <td>Reported as shark attack but probable drowning</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>2449</th>
      <td>1969</td>
      <td>Invalid</td>
      <td>Russian male</td>
      <td>M</td>
      <td>FATAL</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>3280</th>
      <td>1967</td>
      <td>Provoked</td>
      <td>Romeo Guarini</td>
      <td>M</td>
      <td>Diver shot the shark, then it injured his arm ...</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>3435</th>
      <td>1964</td>
      <td>Invalid</td>
      <td>Giancarlo Griffon</td>
      <td>M</td>
      <td>Disappeared, probable drowning but sharks in a...</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>3901</th>
      <td>1958</td>
      <td>Provoked</td>
      <td>Fishing boat. Occupants: Yunus Potur &amp; Ali Durmaz</td>
      <td>N.A.</td>
      <td>Boat damaged</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>4107</th>
      <td>1954</td>
      <td>Provoked</td>
      <td>10 crew</td>
      <td>M</td>
      <td>No injury to occupants. Shark tore nets &amp; traw...</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>4112</th>
      <td>1954</td>
      <td>Invalid</td>
      <td>male</td>
      <td>N.A.</td>
      <td>Human remains found in shark</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>4693</th>
      <td>1935</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>human remains washed ahore</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5307</th>
      <td>1901</td>
      <td>Invalid</td>
      <td>Antonio Tornatori</td>
      <td>M</td>
      <td>Disappeared, but shark involvement unconfirmed</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5437</th>
      <td>1892</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>No injury, no attack</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5461</th>
      <td>1890</td>
      <td>Invalid</td>
      <td>Joseph Lundy</td>
      <td>M</td>
      <td>Forensic evidence indicated death resulted fro...</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5468</th>
      <td>1889</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Human remains found in 4m, 900 kg shark</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5642</th>
      <td>1872</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>No injury</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5699</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Possible drowning and scavenging</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5718</th>
      <td>1859</td>
      <td>Unprovoked</td>
      <td>J.G. Luther</td>
      <td>M</td>
      <td>FATAL</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5747</th>
      <td>1852</td>
      <td>Invalid</td>
      <td>Karen Bredesen Str\E6te</td>
      <td>F</td>
      <td>Death preceded shark involvement</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5793</th>
      <td>1837</td>
      <td>Invalid</td>
      <td>adult male, a sailor</td>
      <td>M</td>
      <td>Shark caught contained human remains</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5794</th>
      <td>1836</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Shark caught, contained human remains</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5820</th>
      <td>1818</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Probable drowning</td>
      <td>UNDETERMINED</td>
    </tr>
    <tr>
      <th>5849</th>
      <td>1733</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Partial hominid remains recovered from shark, ...</td>
      <td>UNDETERMINED</td>
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
      <th>Type</th>
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
      <td>Unprovoked</td>
      <td>female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1047</th>
      <td>2008</td>
      <td>Unprovoked</td>
      <td>Jamie Adlington</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>1142</th>
      <td>2007</td>
      <td>Invalid</td>
      <td>Alex Takyi</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2025</th>
      <td>1997</td>
      <td>Unprovoked</td>
      <td>Jos\E9 Luiz Lipiani</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2035</th>
      <td>1997</td>
      <td>Unprovoked</td>
      <td>Gersome Perreno</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2042</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Blair Hall</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2070</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Trimurti Day</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2082</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Wayne Leong</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2098</th>
      <td>1996</td>
      <td>Unprovoked</td>
      <td>Marris</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2103</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>Carlton Taniyama</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2163</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>Hutchins</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2179</th>
      <td>1995</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2184</th>
      <td>1994</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2317</th>
      <td>1992</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2423</th>
      <td>1990</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2425</th>
      <td>1989</td>
      <td>Unprovoked</td>
      <td>Ryan Johnson</td>
      <td>M</td>
      <td>No details, "recovering in Darwin Hospital"</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2436</th>
      <td>1989</td>
      <td>Unprovoked</td>
      <td>John Benson</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2581</th>
      <td>1986</td>
      <td>Unprovoked</td>
      <td>Crawford</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2657</th>
      <td>1984</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2675</th>
      <td>1984</td>
      <td>Unprovoked</td>
      <td>Greenwood</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2718</th>
      <td>1983</td>
      <td>Unprovoked</td>
      <td>Arnold Schwarzwood</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2771</th>
      <td>1982</td>
      <td>Provoked</td>
      <td>Giovanni Vuoso</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2773</th>
      <td>1982</td>
      <td>Unprovoked</td>
      <td>English holiday-maker</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2781</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>Robert Conklin</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2813</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2816</th>
      <td>1981</td>
      <td>Unprovoked</td>
      <td>Filmer</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>2982</th>
      <td>1975</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3073</th>
      <td>1973</td>
      <td>Unprovoked</td>
      <td>G. Cole</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3171</th>
      <td>1970</td>
      <td>Unprovoked</td>
      <td>David Vota</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>3186</th>
      <td>1970</td>
      <td>Unprovoked</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>4977</th>
      <td>1923</td>
      <td>Invalid</td>
      <td>John Hayes</td>
      <td>M</td>
      <td>Death may have been due to drowning</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>4987</th>
      <td>1922</td>
      <td>Invalid</td>
      <td>H.R.W.</td>
      <td>M</td>
      <td>FATAL, but shark involvement prior to death un...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5014</th>
      <td>1921</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>Buttons &amp; shoes found in shark caught in fish ...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5038</th>
      <td>1919</td>
      <td>Invalid</td>
      <td>5 cadets from the Naval training ship Tingara</td>
      <td>M</td>
      <td>Shark involvement not confirmed</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5097</th>
      <td>1915</td>
      <td>Invalid</td>
      <td>Remains of male found in shark</td>
      <td>M</td>
      <td>Fatal, drowning or scavenging</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5114</th>
      <td>1914</td>
      <td>Unprovoked</td>
      <td>Indian female</td>
      <td>F</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5120</th>
      <td>1913</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>M</td>
      <td>Man's leg recovered from 800-lb shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5121</th>
      <td>1913</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>F</td>
      <td>Female foot recovered from shark</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5134</th>
      <td>1912</td>
      <td>Invalid</td>
      <td>arm recovered from hooked shark</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5173</th>
      <td>1910</td>
      <td>Unprovoked</td>
      <td>Lieut. James H. Stewart</td>
      <td>M</td>
      <td>Calf removed, not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5308</th>
      <td>1901</td>
      <td>Invalid</td>
      <td>boy</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5316</th>
      <td>1900</td>
      <td>Unprovoked</td>
      <td>George Brown</td>
      <td>M</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5355</th>
      <td>1898</td>
      <td>Invalid</td>
      <td>male</td>
      <td>M</td>
      <td>Unknown</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5373</th>
      <td>1897</td>
      <td>Unprovoked</td>
      <td>Anonymous</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5411</th>
      <td>1894</td>
      <td>Unprovoked</td>
      <td>Catherine Beach</td>
      <td>F</td>
      <td>No injury</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5414</th>
      <td>1894</td>
      <td>Unprovoked</td>
      <td>Erskine H. Reynolds</td>
      <td>M</td>
      <td>"Painfully injured" but no details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5432</th>
      <td>1893</td>
      <td>Unprovoked</td>
      <td>No details</td>
      <td>N.A.</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5464</th>
      <td>1890</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5465</th>
      <td>1890</td>
      <td>Unprovoked</td>
      <td>a pearl diver</td>
      <td>M</td>
      <td>No details</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5697</th>
      <td>1862</td>
      <td>Invalid</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5726</th>
      <td>1856</td>
      <td>Unprovoked</td>
      <td>a seaman from the John and Lucy</td>
      <td>M</td>
      <td>Severe bite to thigh. Not known if he survived</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5795</th>
      <td>1836</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>N.A.</td>
      <td>No details, it was the year the first settlers...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5845</th>
      <td>1755</td>
      <td>Unprovoked</td>
      <td>Fishermen</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5856</th>
      <td>1638</td>
      <td>Unprovoked</td>
      <td>sailors</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5857</th>
      <td>1637</td>
      <td>Unprovoked</td>
      <td>Hindu pilgrims</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5858</th>
      <td>1617</td>
      <td>Unprovoked</td>
      <td>Indian people</td>
      <td>N.A.</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5860</th>
      <td>1595</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>Leg severed mid-thigh, hand severed, arm above...</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5862</th>
      <td>1555</td>
      <td>Unprovoked</td>
      <td>male</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5863</th>
      <td>1554</td>
      <td>Unprovoked</td>
      <td>males (wearing armor)</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>male, the Sergeant of Marines</td>
      <td>M</td>
      <td>NaN</td>
      <td>UNKNOWN</td>
    </tr>
  </tbody>
</table>
<p>94 rows × 6 columns</p>
</div>


    {'Y', 'N', 'UNKNOWN', 'UNDETERMINED'}
    Fatal (Y/N) 4



```python
#Genero nuevo Dataset antes de aplicar los filtros y acotar los registros.
df7 = df6.copy()
```


```python
#Se eliminan los registros que no aportan información útil al análisis (5992 rows --> 4821 rows)
display(df7[['Year','Type','Sex ','Fatal (Y/N)']])
df8 = df7.drop(df7[(df7.Year < 1500) | (df7['Type'] == 'Invalid') | (df7['Sex '] == 'N.A.') | (df7['Fatal (Y/N)'] == 'UNDETERMINED') | (df7['Fatal (Y/N)'] == 'UNKNOWN')].index)
display(df8[['Year','Type','Sex ','Fatal (Y/N)']])
#display(df7.loc[df6['Type']=='Unprovoked',['Year','Type','Sex ','Fatal (Y/N)']])
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
      <th>Type</th>
      <th>Sex</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>N.A.</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>N.A.</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5962</th>
      <td>0</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5963</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5964</th>
      <td>0</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5965</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5966</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5967</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>UNKNOWN</td>
    </tr>
    <tr>
      <th>5968</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>N.A.</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5969</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5970</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5971</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5972</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5973</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5974</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5975</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5976</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5977</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>N.A.</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5978</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5979</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5980</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5981</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5982</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5983</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5984</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5985</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5986</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5987</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5988</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5989</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5990</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5991</th>
      <td>0</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>5992 rows × 4 columns</p>
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
      <th>Type</th>
      <th>Sex</th>
      <th>Fatal (Y/N)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>N</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5816</th>
      <td>1825</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5821</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5822</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5823</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5824</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5826</th>
      <td>1812</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5827</th>
      <td>1811</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5828</th>
      <td>1807</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5831</th>
      <td>1803</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5832</th>
      <td>1800</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5833</th>
      <td>1791</td>
      <td>Unprovoked</td>
      <td>F</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5835</th>
      <td>1787</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5836</th>
      <td>1785</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5837</th>
      <td>1779</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5838</th>
      <td>1776</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5840</th>
      <td>1771</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5842</th>
      <td>1764</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5843</th>
      <td>1758</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5844</th>
      <td>1749</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5846</th>
      <td>1748</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5847</th>
      <td>1742</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5848</th>
      <td>1738</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5850</th>
      <td>1721</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5851</th>
      <td>1703</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5852</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5853</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>N</td>
    </tr>
    <tr>
      <th>5854</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5859</th>
      <td>1642</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5861</th>
      <td>1580</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>5864</th>
      <td>1543</td>
      <td>Unprovoked</td>
      <td>M</td>
      <td>Y</td>
    </tr>
  </tbody>
</table>
<p>4821 rows × 4 columns</p>
</div>



```python
#Se crean 'bins' de datos para separar los mismos en 3 eras diferentes para comparar entre ellas.
age_labels = ['Pre-Industrial', 'Industrial', 'Digital']
cutoffs = [1500,1880,1950,2019]
age_bins = pd.cut(df8['Year'],cutoffs, labels=age_labels)
age_bins.head()
```




    0    Digital
    1    Digital
    2    Digital
    3    Digital
    4    Digital
    Name: Year, dtype: category
    Categories (3, object): [Pre-Industrial < Industrial < Digital]




```python
#Elimino columnas que no serán utilizadas y no aportan ninguna descripción relevante para el análisis y se crea
#nuevo dataset que incluye la nueva categorización.
col_f4 = ['Date','Country','Area','Location','Name','original order']
df9 = df8.drop(col_f4, axis=1) 
df9['Ages'] = age_bins
df9.head(6000)
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
      <th>Type</th>
      <th>Activity</th>
      <th>Sex</th>
      <th>Injury</th>
      <th>Fatal (Y/N)</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Minor injury to thigh</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Lacerations to hands</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Lacerations to lower leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Struck by fin on chest &amp; leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>No injury: Knocked off board by shark</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Wading</td>
      <td>M</td>
      <td>Minor injury to arm</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>F</td>
      <td>Severe lacerations to shoulder &amp; forearm</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Kite surfing</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Boogie boarding</td>
      <td>F</td>
      <td>Lacerations &amp; punctures to lower right leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>No inury, board broken in half by shark</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Body boarding</td>
      <td>M</td>
      <td>Foot bitten</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Spearfishing</td>
      <td>M</td>
      <td>Two toes broken &amp; lacerated</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Lacerations to right foot</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Right arm severed, ankle severely bitten</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Wading</td>
      <td>M</td>
      <td>Minor injury to ankle</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Snorkeling</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>SUP Foil boarding</td>
      <td>M</td>
      <td>No inury, shark &amp; board collided</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Big toe bitten</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>Lacerations to right hand</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>Lacerations to leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Kayaking</td>
      <td>M</td>
      <td>No injury, shark nudged kayak repeatedly</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Lobstering</td>
      <td>M</td>
      <td>Laceration to left forearm PROVOKED INCIDENT</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>No injury. Leg rope severed, knocked off board...</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Lacerations to left leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>Calf bumped but no injury</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Spearfishing</td>
      <td>M</td>
      <td>Lacerations to face and right leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016</td>
      <td>Provoked</td>
      <td>Fishing</td>
      <td>M</td>
      <td>Laceration to left calf from hooked shark PROV...</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>30</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>F</td>
      <td>Minor injury to leg</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2016</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>F</td>
      <td>Minor injury to toes</td>
      <td>N</td>
      <td>Digital</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>5816</th>
      <td>1825</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5821</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5822</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5823</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5824</th>
      <td>1817</td>
      <td>Unprovoked</td>
      <td>Conch diver</td>
      <td>M</td>
      <td>Abdomen bitten</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5826</th>
      <td>1812</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>Both legs injured</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5827</th>
      <td>1811</td>
      <td>Unprovoked</td>
      <td>Fell overboard</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5828</th>
      <td>1807</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>M</td>
      <td>Survived</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5831</th>
      <td>1803</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>M</td>
      <td>Shark knocked him down &amp; tore clothing of the ...</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5832</th>
      <td>1800</td>
      <td>Unprovoked</td>
      <td>a corsair's boat was overturned</td>
      <td>F</td>
      <td>FATAL, all onboard were killed by sharks</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5833</th>
      <td>1791</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>F</td>
      <td>FATAL, "bitten in two"</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5835</th>
      <td>1787</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5836</th>
      <td>1785</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>M</td>
      <td>Human remains recovered from shark</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5837</th>
      <td>1779</td>
      <td>Unprovoked</td>
      <td>Surfing</td>
      <td>M</td>
      <td>FATAL, buttock lacerated</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5838</th>
      <td>1776</td>
      <td>Unprovoked</td>
      <td>Murder</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5840</th>
      <td>1771</td>
      <td>Unprovoked</td>
      <td>Fishing</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5842</th>
      <td>1764</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5843</th>
      <td>1758</td>
      <td>Unprovoked</td>
      <td>Fell overboard from a frigate &amp; was swallowed ...</td>
      <td>M</td>
      <td>"He was taken up alive and but little injured."</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5844</th>
      <td>1749</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>Right leg severed at knee.  In 1796 he became ...</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5846</th>
      <td>1748</td>
      <td>Unprovoked</td>
      <td>Pearl diving</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5847</th>
      <td>1742</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5848</th>
      <td>1738</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5850</th>
      <td>1721</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL,  partial remains recovered from shark\9...</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5851</th>
      <td>1703</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>Hand and foot severely bitten, surgically ampu...</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5852</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>NaN</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5853</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>Bathing</td>
      <td>M</td>
      <td>Leg severed</td>
      <td>N</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5854</th>
      <td>1700</td>
      <td>Unprovoked</td>
      <td>Bathing</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5859</th>
      <td>1642</td>
      <td>Unprovoked</td>
      <td>Swimming</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5861</th>
      <td>1580</td>
      <td>Unprovoked</td>
      <td>Man fell overboard from ship. Those on board t...</td>
      <td>M</td>
      <td>FATAL. "Shark tore him to pieces.</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
    <tr>
      <th>5864</th>
      <td>1543</td>
      <td>Unprovoked</td>
      <td>Pearl diving</td>
      <td>M</td>
      <td>FATAL</td>
      <td>Y</td>
      <td>Pre-Industrial</td>
    </tr>
  </tbody>
</table>
<p>4821 rows × 7 columns</p>
</div>




```python
#Creo fichero .csv antes de hacer comparativa
df9.to_csv('/home/potacho/github/datamad0119/module-1/pandas-project/your-code/df9.csv', index=False, encoding = 'utf-8')
```


```python
#Contabilizo los datos generales para cada atributo
types = df9.groupby('Type').Type.count()
#fatal = df9.groupby('Fatal (Y/N)').df9['Fatal (Y/N)'].count()
#sex = df9.groupby('Sex ').df9['Sex '].count()
#(no funciona porque tengo que cambiar nombre de la columna para que funcione count, pero no me ha dado tiempo)
ages = df9.groupby('Ages').Ages.count()
print(types)
#print(fatal)
#print(sex)
print(ages)
```

    Type
    Provoked       744
    Unprovoked    4077
    Name: Type, dtype: int64
    Ages
    Pre-Industrial     235
    Industrial        1077
    Digital           3509
    Name: Ages, dtype: int64



```python
df_type = pd.get_dummies(df9['Type'])
display(df_type[(df9['Ages']=='Digital')].sum())
display(df_type[(df9['Ages']=='Industrial')].sum())
display(df_type[(df9['Ages']=='Pre-Industrial')].sum())
```


    Provoked       495
    Unprovoked    3014
    dtype: int64



    4821



    Provoked      225
    Unprovoked    852
    dtype: int64



    Provoked       24
    Unprovoked    211
    dtype: int64



```python
df_fatal = pd.get_dummies(df9['Fatal (Y/N)'])
display(df_fatal[(df9['Ages']=='Digital')].sum())
display(df_fatal[(df9['Ages']=='Industrial')].sum())
display(df_fatal[(df9['Ages']=='Pre-Industrial')].sum())
```


    N    2967
    Y     542
    dtype: int64



    N    608
    Y    469
    dtype: int64



    N    101
    Y    134
    dtype: int64



```python
df_sex = pd.get_dummies(df9['Sex '])
display(df_sex[(df9['Ages']=='Digital')].sum())
display(df_sex[(df9['Ages']=='Industrial')].sum())
display(df_sex[(df9['Ages']=='Pre-Industrial')].sum())
```


    F     443
    M    3066
    dtype: int64



    F      57
    M    1020
    dtype: int64



    F     12
    M    223
    dtype: int64


### Conclusiones
Se ha podido establecer un análisis de la evolución de la influencia humana en la incidencia de ataques de tiburones.
