def benixLite(arr):

    print(arr)
    noBracks= arr[1:-1]
    print(noBracks)
    list = [int(s) for s in noBracks.split(",")]
    print(list)
    print(type(list))
    def bubblesort(list):
        for iter_num in range(len(list)-1,0,-1):
            for idx in range(iter_num):
                if list[idx]>list[idx+1]:
                     temp = list[idx]
                     list[idx] = list[idx+1]
                     list[idx+1] = temp
    bubblesort(list)
    return list