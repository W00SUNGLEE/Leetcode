class MyHashMap:

    def __init__(self):
        self.hashMap = []
        

    def put(self, key: int, value: int) -> None:
        #print("key: {}, value: {}".format(key, value))
        #print("len(hashMap): {}".format(len(self.hashMap)))
        
        for i in range(len(self.hashMap)):
            #print(self.hashMap[i][0], key)
            if self.hashMap[i][0] == key:
                self.hashMap[i][1] = value
                #print(self.hashMap[i])
                return
        
        self.hashMap.append([key, value])
        return

    def get(self, key: int) -> int:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                return self.hashMap[i][1]
            
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap)):
            if self.hashMap[i][0] == key:
                self.hashMap.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)