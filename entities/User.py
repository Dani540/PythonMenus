class User:
        
    def __init__(self, name):
        self.name = name
        self.items = {
            "Pizza" : [],
            "Bebida" : [],
            "Galleta" : []
        }

    def __str__(self):
        return f"\n-------------------- \nname: {self.name} \nitems: {self.items} --------------------"

    def addItem(self, item): 
        self.items[item.type].append(item.name)
        
    def addItems(self, *args):
        for i in args: self.addItem(i)
        
    def itemsToString(self):
        aux = "\n"
        for clave, valor in self.items.items():
            valStr = "\n| - ".join(valor)
            aux += "| " + str(clave) + " :\n| - " + valStr + "\n"
        return aux
