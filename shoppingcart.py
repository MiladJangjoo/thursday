
# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list

def shopping_cart ():
    cart = {}
    while True:
        data = input("show/add/delete or quit?")
        if data =="show":
            print(cart)
        if data == "add":
            key = input ("what do you want to add?")
            value = input ("whats the quantity?")
            cart[key] = value
        if data == "delete":
            pak = input ("what do you want to delete?")
            # cart.pop(pak)
            del cart[pak] 
        if data == "quit":
            break
    return cart
shopping_cart ()