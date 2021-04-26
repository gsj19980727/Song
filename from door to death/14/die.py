#!/usr/bin/env python
# coding: utf-8

# In[3]:


from random import randint
class Die():
    '''表示一个骰子的类'''
    
    def __init__(self, num_sides = 6):
        '''骰子默认为6面'''
        self.num_sides = num_sides
        
    def  roll(self):
        '''返回一个位于1和骰子面数之间的随机值'''
        return randint(1, self.num_sides)


# In[4]:


try:    
    get_ipython().system('jupyter nbconvert --to python die.ipynb')
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass


# In[ ]:




