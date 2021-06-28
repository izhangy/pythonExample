# -*- coding: UTF-8 -*-

"""
@File: dict.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 18:06
"""
m_dict = {
    'a':{
        'b':{
            'c':'hi'
        }
    }
}
print(m_dict['a']['b']['c'])

#第一种

scores={'name':'zhang', 'age':2}
print(scores)
#第二种

scores=dict(name='zhang',age=2)

print(scores)