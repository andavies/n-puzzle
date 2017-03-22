from collections import deque

class Frontier:
        
    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        for element in self.queue:
            if item.state == element.state:
                return True

        return False



class Explored:
       
    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        for element in self.set:
            if item.state == element.state:
                return True

        return False
        
    

        
