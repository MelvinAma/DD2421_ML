import monkdata as m
import dtree as d

'''
Assignment 1:
1.0
0.957117428264771
0.9998061328047111
'''

for i in [m.monk1, m.monk2, m.monk3]:
    print(d.entropy(i))
