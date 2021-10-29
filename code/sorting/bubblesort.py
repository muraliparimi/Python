def bubble_sort(items):
    for i in range(len(items)):
        already_sorted=True
        for j in range(len(items)-i-1):
            if items[j] >items[j+1]:
                items[j],items[j+1] = items[j+1],items[j]
                already_sorted=False
        if already_sorted:
            break
    return items



if __name__ == '__main__':
    print(bubble_sort([8,5,2,9,1,7,10,20,8,11,6,19,18,15]))
    print(bubble_sort([1,2,3,4,5]))