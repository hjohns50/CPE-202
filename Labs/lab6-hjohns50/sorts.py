import random
import time

def selection_sort(lst):
    cmp = 0
    for i in range(len(lst) - 1):
        min_spot = i
        for j in range(i+1, len(lst)):
            cmp += 1
            if lst[j] < lst[min_spot]:
                   min_spot = j
        if i != min_spot:
            swap(lst, i, min_spot)
    return cmp
def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    
def insertion_sort(alist): 
    comparisons = 0
    if len(alist) == 0:
        return 0
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            comparisons += 1
            alist[position] = alist[position-1]
            position = position-1

        if alist[position-1] < currentvalue:
            comparisons += 1
        alist[position] = currentvalue
    return comparisons
    
def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

