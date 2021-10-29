#from timing import timed_func
import random

#@timed_func
def insert_sort(items):
    for i in range(1, len(items)):
        current_item=items[i]
        j=i-1

        while (j>=0 and current_item < item[j]): 
            items[j+1] = items[j]
            j -= 1
        items[j+1] = current_item
    return items




if __name__ == '__main__':
    items = [random.randint(1,1000) for _ in range(1000)]
    print(insert_sort(items))