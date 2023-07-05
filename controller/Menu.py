from entities.Item import Item

class Menu:
    
    def __init__(self, title):
        self.title = title
        self.items = {}     
        self.count = 0
    
    def addItem(self, item):
           self.items[self.count] = item
           self.count+=1
           
    def addItems(self, *args):
        for i in args: self.addItem(i)
        
    def getItems(self):
        return self.items
    
    def printOptions(self):
        for i in self.items:
            aux = i+1 # Solo para que se vea mas bonito lkdjslkds
            print(str(aux) + " - " + str(self.items[i]))
            
    def showAndWait(self):
        print("------------------------")
        self.printOptions()
        print("------------------------\nChoose: ")
        op = 0
        while(True):
            try: 
                op = int(input())
                break
            except ValueError:
                print("Invalid Input Type!")  
            
        while op > len(self.items) or op <= 0:
            print("Invalid range!")
            op = int(input())
        return self.items[op - 1]
