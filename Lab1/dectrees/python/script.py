import monkdata as m
import dtree as d

'''
Assignment 1:
1.0
0.957117428264771
0.9998061328047111
'''
print("\n" + "-" * 10 + "\n")
print("Assignment 1:\n")
for i in [m.monk1, m.monk2, m.monk3]:
    print(d.entropy(i))

'''
Assignment 2:
[BARA TEXT]
'''

'''
Assignment 3:
MONK-1
0.07527255560831925
0.005838429962909286
0.00470756661729721
0.02631169650768228
0.28703074971578435
0.0007578557158638421
MONK-2
0.0037561773775118823
0.0024584986660830532
0.0010561477158920196
0.015664247292643818
0.01727717693791797
0.006247622236881467
MONK-3
0.007120868396071844
0.29373617350838865
0.0008311140445336207
0.002891817288654397
0.25591172461972755
0.007077026074097326
'''
print("\n" + "-" * 10 + "\n")
print("Assignment 3:\n")
for i in [m.monk1, m.monk2, m.monk3]:
    print(f"MONK-{[m.monk1, m.monk2, m.monk3].index(i) + 1}")
    for j in range(6):
        print(d.averageGain(i, m.attributes[j]))

'''
Assignment 4:
[BARA TEXT]
'''


'''
Assignment 5:
[fill]
'''
print("\n" + "-" * 10 + "\n")
print("Assignment 5:\n")


'''
Assignment 6:
[BARA TEXT]
'''


'''
Assignment 7:
[fill]
'''
print("\n" + "-" * 10 + "\n")
print("Assignment 7:\n")
