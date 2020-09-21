import sys
import random


def benix(txt,other):
    randomlist = []
    for i in range(0,int(other)):
        n = random.randint(1,30)
        randomlist.append(n)
    print(randomlist)
    print(other)
    list = [int(s) for s in txt.split()]

    lost = []
    def bubblesort(list):

# Swap the elements to arrange in order
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                termp = list.copy()
                lost.insert(len(lost), termp)
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
    bubblesort(randomlist)
    return lost
# print(list)