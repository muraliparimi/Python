import random
import time

def merge_sorted_lists(left,right):
    left_index, right_index = 0, 0
    return_list=[]
    while (len(return_list) < len(left) + len(right)):
        left_item = left[left_index] if left_index < len(left) else float('inf')
        right_item = right[right_index] if right_index < len(right) else float('inf')
        if (right_item < left_item):
            return_list.append(right_item)
            right_index +=1
        else:
            return_list.append(left_item)
            left_index +=1
    return return_list
    

def merge_sort(items):
    n= len(items)//2
    if n <=1:
        return items
    midpoint = n//2
    left,right = items[:midpoint],items[midpoint:]
    return merge_sorted_lists(merge_sort(left),merge_sort(right))


if __name__ == '__main__':
    rand_list = [random.randint(1,1000) for _ in range(1000000)]
    start = time.perf_counter()
    merge_sort(rand_list)
    print(time.perf_counter() - start)