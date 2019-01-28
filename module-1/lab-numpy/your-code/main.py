#!/usr/bin/env python
# coding: utf-8

# In[184]:


#1. Import the NUMPY package under the name np.
import numpy as np


# In[185]:


#2. Print the NUMPY version and the configuration.
print(np.__version__)
print(np.show_config())


# In[186]:


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. 
#How many ways can you find?
a = np.random.random((2,3,5))
#a = np.random.random_sample((2,3,5))
#a = np.random.ranf((2,3,5))
#No vemos ninguna diferencia a simple vista.


# In[187]:


#4. Print a.
print(a)


# In[188]:


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


# In[189]:


#6. Print b.
print(b)


# In[190]:


#7. Do a and b have the same size? How do you prove that in Python code?
len_a = a.size
len_b = b.size
#print(len_a)
#print(len_b)
if len_a == len_b:
    print("a size es igual a b size")


# In[191]:


#8. Are you able to add a and b? Why or why not?
print(np.add(a, b))
#ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3). No se pueden sumar al 
#tener diferentes dimensiones


# In[225]:


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). 
#Assign the transposed array to varialbe "c".
c = np.reshape(b, (2,3,5))
print(c)


# In[228]:


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = np.add(a, c)
print(d)
#Now a and d have the same shape


# In[229]:


#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
#La diferencia es que en 'd' se ha sumado a cada valor de 'a' el valor '1'.


# In[230]:


#12. Multiply a and c. Assign the result to e.
e = np.multiply(a, c)
print(e)


# In[231]:


#13. Does e equal to a? Why or why not?
print(a)
print(e)
np.array_equal(a,e)

#Son iguales porque e multiplica los valores de 'a' por 'c' que es una matriz equivalente en forma a 'a' pero 
#con cada valor =1


# In[232]:


#14. Identify the max, min, and mean values in 'd'. Assign those values to variables "
#d_max", "d_min", and "d_mean"
d_max = np.amax(d)
d_min = np.amin(d)
d_mean = np.mean(d)
print(d_max, d_min, d_mean)


# In[233]:


#15. Now we want to label the values in 'd'. 
#First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty([2,3,5])
print(f.shape)


# In[288]:


#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, 
#assign 25 to the corresponding value in f.
#If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
#If a value equals to d_mean, assign 50 to the corresponding value in f.
#Assign 0 to the corresponding value(s) in f for d_min in d.
#Assign 100 to the corresponding value(s) in f for d_max in d.
#In the end, f should have only the following values: 0, 25, 50, 75, and 100.
#Note: you don't have to use Numpy in this question.

f = np.array(d)
f[(d > d_min) & (d < d_mean)] = 25
f[(d < d_max) & (d > d_mean)] = 75
f[(d == d_mean)] = 50
f[(d == d_min)] = 0
f[(d == d_max)] = 100


# In[289]:


#17. Print d and f. Do you have your expected f?
print(d)
print(f)


# In[290]:


# 18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
f1 = f.reshape(30)
g = f1.tolist()
for i in range(len(g)):
    if g[i] == 25:
        g[i] = "B"
    elif g[i] == 75:
        g[i] = "D"
    elif g[i] == 50:
        g[i] = "C"
    elif g[i] == 0:
        g[i] = "A"
    elif g[i] == 100:
        g[i] = "E"
g1 = np.asarray(g)
g2 = g1.reshape(2,3,5)
print(g2)

