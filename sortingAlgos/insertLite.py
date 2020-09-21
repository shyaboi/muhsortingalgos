
def insertLite(InputList):
    noBracks= InputList[1:-1]
    InputList = [int(s) for s in noBracks.split(",")]
    print(InputList)
    def insertion_sort(InputList):
        for i in range(1, len(InputList)):
            j = i-1
            nxt_element = InputList[i]
    # Compare the current element with next one
            
            while (InputList[j] > nxt_element) and (j >= 0):
                InputList[j+1] = InputList[j]
                j=j-1
            InputList[j+1] = nxt_element

    insertion_sort(InputList)
    return InputList