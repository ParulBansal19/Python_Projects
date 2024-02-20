#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import plotly.express as ps
import plotly.graph_objects as go


# In[5]:


apple= pd.read_csv("apple_products.csv")


# In[6]:


apple


# In[7]:


apple.describe()


# In[8]:


print(apple.isnull().sum())


# # Iphone sales analysis in India

# # Based on star ratings

# In[9]:


highest_rated= apple.sort_values(by= ["Star Rating"], ascending= False)
highest_rated= highest_rated.head(10)
print(highest_rated["Product Name"])


# # Lets have a look at the number of ratings of the highest rated iphone on flipkart

# In[10]:


iphones= highest_rated["Product Name"].value_counts()
label= iphones.index
counts= highest_rated["Number Of Ratings"]
figure= ps.bar(highest_rated, x= label, y= counts, title= "Number of ratings of highest rated iphones")
figure.show()


# According to the above bar graph, Apple iphone 8 Plus(Gold, 64 GB) has the most rating on Flipkart. 

# # Lets have a look at the number of reviews of the highest rated iphone on flipkart

# In[11]:


iphones= highest_rated["Product Name"].value_counts()
label= iphones.index
counts= highest_rated["Number Of Reviews"]
figure= ps.bar(highest_rated, x= label, y= counts, title= "Number of reviews of highest rated iphones")
figure.show()


# Apple iphone 8 Plus(Gold, 64GB) is also leading in the highest number of reviews on Flipkart among the highest- rated iphones in india.

# # Let's have a look at the relationship between the sale price of iphones and their ratings on flipkart

# In[12]:


figure= ps.scatter(data_frame= apple, x= "Number Of Ratings", y= "Sale Price", 
                   size= "Discount Percentage", trendline= "ols", title= "Relationship between sale price & number of ratings" )
figure.show()


# There is a negative linear relationship between the sale price of iphones and the number of ratings. it means iphones with lower sale prices are sold more in india.

# # Let's have a look at the Relationship Between Discount Percentage on iphones & Number of Ratings:

# In[13]:


figure= ps.scatter(data_frame= apple, x= "Number Of Ratings", y= "Discount Percentage", 
                   title= "Relationship between discount percentage & number of ratings", size= "Sale Price", trendline= "ols")
figure.show()


# # Summary:

# Apple Iphone 8 Plus(Gold, 64GB) was the most appreciated iphone in india iphones with lower sale price are sold more in india iphones with high discounts are sold more in india.

# In[ ]:




