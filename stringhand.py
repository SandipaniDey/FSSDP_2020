# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:54:33 2020

@author: SAMD
"""


name=input('Enter name: ')
x=name.rsplit()
y=x[0],x[1]=x[1],x[0]
z=' '.join(y)
print(z)