#!/usr/bin/env python
# coding: utf-8

# In[107]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[108]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


# In[109]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. 
#How many ways can you find?
a = np.random.random((2,3,5))
#a = np.random.random_sample((2,3,5))
#a = np.random.ranf((2,3,5))
#No vemos ninguna diferencia a simple vista.


# In[110]:


#4. Print a.
print(a)


# In[111]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


# In[112]:


#6. Print b.
print(b)


# In[113]:


#7. Do a and b have the same size? How do you prove that in Python code?
len_a = a.size
len_b = b.size
#print(len_a)
#print(len_b)
if len_a == len_b:
    print("a size es igual a b size")


# In[114]:


#8. Are you able to add a and b? Why or why not?
print(np.add(a, b))
#ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3). No se pueden sumar al 
#tener diferentes dimensiones


# In[125]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). 
#Assign the transposed array to varialbe "c".
c = np.reshape(b, (2,3,5))
print(c)


# In[126]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a, c)
print(d)
#Now a and d have the same shape


# In[127]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
#La diferencia es que en 'd' se ha sumado a cada valor de 'a' el valor '1'.


# In[128]:


#12. Multiply a and c. Assign the result to e.
e = np.multiply(a, c)
print(e)


# In[129]:


#13. Does e equal to a? Why or why not?
print(a)
print(e)
np.array_equal(a,e)

#Son iguales porque e multiplica los valores de 'a' por 'c' que es una matriz equivalente en forma a 'a' pero 
#con cada valor =1


# In[130]:


#14. Identify the max, min, and mean values in 'd'. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.mean(d)
print(d_max, d_min, d_mean)


# In[131]:


#15. Now we want to label the values in 'd'. 
#First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty([2,3,5])
print(f.shape)


# In[132]:


#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, 
#assign 25 to the corresponding value in f.
#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.

#d1 = np.copy(d)
#print(d1[0][0][0])
#for i in range(0,30):
#    if d1[i][i][i] == d_max:
#        d1[i][i][i] = 0
        
#d2 = np.copy(d)
#d3 = np.copy(d)
#d4 = np.copy(d)
#print(d1,d2,d3,d4)

x = 0
y = 0
z = 0
for i in range(30):
  if x < 2:
    if d_mean < d[x][y][z] and d[x][y][z] < d_max:
      f.insert((x,y,z), 75)
      x += 1
    elif d_mean == d[x][y][z]:
      f.insert((x,y,z), 50)
      x += 1 
    elif d_min == d[x][y][z]:
      f.insert((x,y,z), 0)
      x += 1 
    elif d_max == d[x][y][z]:
      f.insert((x,y,z), 100)
      x += 1
  elif y < 3:
    if d_mean < d[x][y][z] and d[x][y][z] < d_max:
      f.insert((x,y,z), 75)
      x += 1
    elif d_mean == d[x][y][z]:
      f.insert((x,y,z), 50)
      x += 1 
    elif d_min == d[x][y][z]:
      f.insert((x,y,z), 0)
      x += 1 
    elif d_max == d[x][y][z]:
      f.insert((x,y,z), 100)
      x += 1
  elif z < 5:
    if d_mean < d[x][y][z] and d[x][y][z] < d_max:
      f.insert((x,y,z), 75)
      x += 1
    elif d_mean == d[x][y][z]:
      f.insert((x,y,z), 50)
      x += 1 
    elif d_min == d[x][y][z]:
      f.insert((x,y,z), 0)
      x += 1 
    elif d_max == d[x][y][z]:
      f.insert((x,y,z), 100)
      x += 1

print(f)
print(e)


# In[133]:


#17. Print d and f. Do you have your expected f?


# In[134]:


#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 


# In[ ]:




