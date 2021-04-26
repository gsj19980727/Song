#!/usr/bin/env python
# coding: utf-8

# In[17]:


class GameStats():
    '''跟踪游戏的统计信息'''
    
    def __init__(self, ai_settings):
        '''初始化统计信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于非活动状态
        self.game_active = False
        #在任何情况下都不应该重置最高得分
        self.high_score = 0
        
    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


# In[18]:


try:    
    get_ipython().system('jupyter nbconvert --to python game_stats.ipynb')
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass


# In[ ]:




