#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    
    def __init__(self):
        '''初始化游戏的静态设置'''
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230 , 230 , 230)
        #飞船的设置
        self.ship_limit = 3
        
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60 , 60 , 60
        self.bullets_allowed = 3
        
        #外星人设置        
        self.fleet_drop_speed = 10
                
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        
        #记分
        self.alien_points = 50
                
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        
        #fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        
    def increase_speed(self):
        '''提高速度设置和外星人点数'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


# In[20]:


try:    
    get_ipython().system('jupyter nbconvert --to python settings.ipynb')
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass


# In[ ]:




