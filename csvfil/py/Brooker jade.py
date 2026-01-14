#!/usr/bin/env python
# coding: utf-8

# In[4]:


import bokeh
from bokeh.io import output_notebook, show
from bokeh.plotting import figure
output_notebook()


# In[8]:


p = figure(width=700, height=700)
p.multi_polygons(
    xs=[
    [[ [1,1,2.5,2.5], [1.2,1.2,1.6,1.6], [1.6, 1.8, 1.8]], [[1,1,2,2],[1.3,1.3,1.7]], [[3,3,5,5], [3.5,3.5,4.6,4.2] ]]],
             
ys=[
 [[ [3,4,3,4], [3.2, 3.6, 3.2, 3.6], [3.8,3.8,3.4]], [ [1,2,1,2], [1.3,1.6,1.6]], [[1,3,1,3], [1.5,2.5,2.5,1.5] ]]],
    
    
color=['orange', 'green','orange']
                 

)

show(p)


# In[ ]:




