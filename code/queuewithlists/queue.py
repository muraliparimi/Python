class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self,item):
        self.__items.append(item)

    def dequeue(self):
        try:
            return self.__items.pop(0)
        except IndexError:
            print("Empty Queue")
    
    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        print(f"Queue({self.__items})")