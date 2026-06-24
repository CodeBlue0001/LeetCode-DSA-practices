class LRUCache:
    # CACHE={}
    # ORDER=[] # the roder should be in old to new 
    #     MAX=capacity
    def __init__(self, capacity: int):
        self.CACHE={}
        self.ORDER=[] # the roder should be in old to new 
        self.MAX=capacity

    def get(self, key: int) -> int:
        if key in self.CACHE:
           
            self.ORDER.remove(key)
            self.ORDER.append(key)

            # print("GET-",key,'ORDER:',self.ORDER,"CACHE:",self.CACHE,"MAX",self.MAX)
            return self.CACHE[key]
        # print("GET-",key,'ORDER:',self.ORDER,"CACHE:",self.CACHE,"MAX",self.MAX)
        return -1

    def put(self, key: int, value: int) -> None:
        # if len(self.CACHE)<self.MAX:
        #     self.CACHE[key]=value
        #     self.ORDER.append(key)
        if key in self.CACHE.keys():
            self.CACHE[key]=value
            self.ORDER.remove(key)
            self.ORDER.append(key)
        else:
            if len(self.CACHE)>=self.MAX:
                old_key=self.ORDER.pop(0)
                self.CACHE.pop(old_key)
            self.CACHE[key]=value
            self.ORDER.append(key)
            
        # print("PUT",'ORDER:',self.ORDER,"CACHE:",self.CACHE,"MAX",self.MAX)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)