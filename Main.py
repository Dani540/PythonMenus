from entities.Item import Item
from entities.User import User
from controller.Menu import Menu

user = User("Dani")

drink1 = Item("Bebida", "Coca-cola")
drink2 = Item("Bebida", "Fanta")
drink3 = Item("Bebida", "Canada Dry")
drink4 = Item("Bebida", "Sprite")

cook1 = Item("Galleta", "Chocolate")
cook2 = Item("Galleta", "Vainilla")
cook3 = Item("Galleta", "Manzana")

pizz1 = Item("Pizza", "Italiana")
pizz2 = Item("Pizza", "Hawaiana")
pizz3 = Item("Pizza", "Napolitana")

mainMenu = Menu("Main Menu")

pizzaMenu = Menu("Pizza")
cookieMenu = Menu("Cookie")
drinksMenu = Menu("Drinks")

mainMenu.addItems("Pizza", "Cookie", "Drinks")

pizzaMenu.addItems(pizz1, pizz2, pizz3)
cookieMenu.addItems(cook1, cook2, cook3)
drinksMenu.addItems(drink1, drink2, drink3, drink4)

while(True):
    op = mainMenu.showAndWait()

    if (op == "Pizza"): 
        user.addItem(pizzaMenu.showAndWait())
    elif (op == "Cookie"): 
        user.addItem(cookieMenu.showAndWait())
    elif (op == "Drinks"): 
        user.addItem(drinksMenu.showAndWait())    
    print("---------------------")
    print("User Storage: " + user.itemsToString())
