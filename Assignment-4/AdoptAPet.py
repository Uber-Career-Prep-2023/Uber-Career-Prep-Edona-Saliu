'''
Time spent: 45 mins
DataStructure: 2 Queues
Time Complexity: O(1)
Space Complexity: O(n)
'''
 
from collections import deque
import sys

class AdoptAPet:
    def __init__(self):
        self.d = deque()
        self.c = deque()
        self.t = 0  # Time counter to track arrival order

    def add_animal(self, name, species):
        self.t += 1
        if species == 'dog':
            self.d.append((name, self.t))
        elif species == 'cat':
            self.c.append((name, self.t))

    def remove(self):
        if not self.d:
            return self.remove_cat()
        elif not self.c:
            return self.remove_dog()

        if self.d[0][1] < self.c[0][1]:
            return self.remove_dog()
        else:
            return self.remove_cat()

    def remove_dog(self):
        return self.d.popleft()[0] if self.d else None

    def remove_cat(self):
        return self.c.popleft()[0] if self.c else None

    def adopt(self, species):
        if species == 'dog':
            return self.remove_dog() or self.remove_cat()
        elif species == 'cat':
            return self.remove_cat() or self.remove_dog()
        else:
            return self.remove()


if __name__ == "__main__":
    shelter = AdoptAPet()
    # Initial animals in the shelter
    shelter.add_animal('Sadie', 'dog')
    shelter.add_animal('Woof', 'cat')
    shelter.add_animal('Chirpy', 'dog')
    shelter.add_animal('Lola', 'dog')

    print(shelter.adopt('dog'))  

    shelter.add_animal('Floofy', 'cat')  

    print(shelter.adopt('dog')) 

    print(shelter.adopt('cat'))  

    print(shelter.adopt('dog'))  
