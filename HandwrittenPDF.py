#!/usr/bin/env python
# coding: utf-8

# In[7]:


from PIL import Image


# In[8]:


import pytesseract


# In[9]:


import sys


# In[10]:


from pdf2image import convert_from_path


# In[11]:


import os


# In[12]:


PDF_file="Bangalore.pdf"


# In[13]:


pages=convert_from_path(PDF_file,500)


# In[14]:


image_counter=1


# In[15]:


for page in pages:
    filename="page_"+str(image_counter)+".jpg"
    page.save(filename,'JPEG')
    image_counter=image_counter+1
    


# In[16]:


file_limit=image_counter-1


# In[17]:


outfile="out_file.txt"


# In[18]:


f=open(outfile,"a")


# In[22]:


pytesseract.pytesseract.tesseract_cmd=r'C:\Users\ekrimen\AppData\Local\Tesseract-OCR\tesseract.exe'


# In[23]:


for i in range(1,file_limit+1):
    filename="page_"+str(i)+".jpg"
    text=str(pytesseract.image_to_string(Image.open(filename)))
    text=text.replace('-\n','')
    f.write(text)


# In[ ]:




