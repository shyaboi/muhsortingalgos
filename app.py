# import time


# Swap the elements to arrange in order
def bubblesort(list):
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
                forIterList = list
                return forIterList
                # time.sleep(.02) 
                # ifIterList = list
                # print(ifIterList)
# list = [19,2,31,45,6,113,121,5764,27,42,656,88,234,11,765,66]
# bubblesort(list)
# print(list)d