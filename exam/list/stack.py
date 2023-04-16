class Stack:
    def __init__(self):
        self.top = []
        
    def __str__(self):
        return str(self.top)
        
    def isEmpty(self):
        return len(self.top) == 0
    
    def size(self):
        return len(self.top)
    
    def clear(self):
        self.top = []
    
    def push(self, item):
            self.top.append(item)
            
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
            
    def peek(self):    #peek 메소드는 맨 뒤의 항목을 삭제하지 않고 반환한다
        if not self.isEmpty():
            return self.top[-1]
        
        
    