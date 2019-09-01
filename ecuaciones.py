
# In[1]:


print("Ecuaciones 2# grado")


# In[2]:


a = int(input("el valor de x1 es: "))


# In[3]:


b = int(input("el valor de x2 es: "))


# In[4]:


c = int(input("el valor de x3 es: "))


# In[5]:


print("la ecuacion es: " + str(a) + "x^2 + " + str(b) +  "x + "  + str(c) +  " = 0 ")


# In[15]:


if b**2 > (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


# In[16]:


if b**2 < (4*a*c):
    e = 2*a
    d = (b**2 - 4*a*c)**(1/2)
    x1 = (-b + d)/e
    x2 = (-b - d)/e
    print("El resultado es ")
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))


# In[ ]:




