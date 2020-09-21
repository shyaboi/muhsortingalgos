import sys
import random

# benix function for taking in the post arguments and doing the sorting magic, and spitting back an array of arrays
def benix(txt,other):
# decalre random list if no user list was entered
    randomlist = []
    # random list gen for loop
    for i in range(0,int(other)):
      # muh python inclusive/exlusive range
        n = random.randint(1,1001)
        randomlist.append(n)
# lost list alias to return at end of itterations
    lost = []
# if its not blank, the array is the user entered numbers split to an arr
    if txt!='':
      list = [int(s) for s in txt.split()]
      pass
    else:
      # if the user didn't enter any text, the slider determines the indices amount
      list = randomlist
      # the ol' buubble sort this one taken from https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
    def bubblesort(list):
# Swap the elements to arrange in order
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
              # making a temp list copy 
                termp = list.copy()
                lost.insert(len(lost), termp)
                if list[idx]>list[idx+1]:
                    temp = list[idx]
                    list[idx] = list[idx+1]
                    list[idx+1] = temp
    bubblesort(list)
    # returning the array of arrays
    return lost