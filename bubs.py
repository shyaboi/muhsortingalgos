import sys
import random

# benix function for taking in the post arguments and doing the sorting magic, and spitting back an array of arrays
def benix(txt,other):

    randomlist = []
    for i in range(0,int(other)):
        n = random.randint(1,30)
        randomlist.append(n)

    print(randomlist)
    print(other)




    lost = []

    if txt!='':
      list = [int(s) for s in txt.split()]
      pass
    else:
      list = randomlist
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
    bubblesort(list)
    return lost
# print(list)