class MyList:
    def __init__(self):
        self.data = []

    def append(self, item):
        """Add an item to the end of the list"""
        self.data += [item] 

    def delete(self, index):
        """Delete an item by index"""
        if 0 <= index < len(self.data):
            del self.data[index]
        else:
            print("Index out of range!")

    def __len__(self):
        """Return the length of the list"""
        return len(self.data)

    def __getitem__(self, index):
        """Access element by index"""
        return self.data[index]

    def __str__(self):
        """Return string representation of the list"""
        return str(self.data)

mylist = MyList()
mylist.append(10)
mylist.append(20)
mylist.append(30)

print("My List:", mylist)       
print("Length:", len(mylist))   

mylist.delete(1)
print("After deletion:", mylist)  
