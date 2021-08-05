class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
    
    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        
        returned_data = self.heap_array[1]
        return returned_data
#heap = Heap(15)
#heap.insert(10)
#heap.insert(8)
#heap.insert(5)
#heap.insert(4)
#heap.insert(20)
#heap.heap_array
