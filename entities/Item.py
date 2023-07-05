class Item:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        
    def __str__(self):
        return self.type + " - " + self.name