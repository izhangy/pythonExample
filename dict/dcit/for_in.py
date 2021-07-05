# -*- coding: UTF-8 -*-

"""
@File: for_in.py
@Auth ： When all the rain falls, you are still not far away.
@Time ： 2021/6/23 20:14
"""
scores={'zhangsan':100, 'lihua':21, 'lisi':3, 1:1}
#item只会输出键
for item in scores:
    print(item, scores.get(item))

#遍历字典
#1 遍历所有的键值对
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'femi'
}


#for后的两个词按顺序分别是key和value
for key, value in user_0.items():
    print("\nKey:", key)
    print("\nValue: ", value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
#2. 遍历所有的键 dict.keys()
for name in favorite_languages.keys():
    print(name.title())
#遍历字典时，默认遍历字典所有的键，因此直接遍历dict输出的仍为键
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    if name in friends:
        print("Hi", name.title(), ",I see your favorite language is ", favorite_languages.get(name).title() + "!")

#对键进行排序
for name in sorted(favorite_languages.keys()):
    print(name.title(), ", thank you for taking the poll")

#3. 遍历字典中的所有值,考虑到其值的重复性，将遍历到的value放入set中
for language in set(favorite_languages.values()):#集合是不重复无序的集合
    print(language)

"""
字典嵌套：
"""
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]#将三个字典放入一个列表中
for alien in aliens:
    print(alien)

new_aliens = []
#创建30个绿色外星人
for alien in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    new_aliens.append(new_alien)
    #显示前五个外星人
for alien in new_aliens[:5]:
    print(alien)
print("--------")
#显示创建了多少个外星人
print("Total number of aliens: ", str(len(new_aliens)))
