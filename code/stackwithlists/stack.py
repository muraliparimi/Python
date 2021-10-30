class Stack:
    def __init__(self):
        self.__items = []
    
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            print("Emptty stack")
    
    def __len__(self):
        return len(self.__items)

    def __repr__(self):
        return f"Stack({self.__items})" 


if __name__ == '__main__':
    s1=Stack()
    for i in range(1,11):
        s1.push(i)
    print(s1)